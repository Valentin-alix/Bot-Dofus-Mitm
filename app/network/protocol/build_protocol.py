import json
import os
import pickle
import re
from copy import deepcopy
from pathlib import Path

from tqdm import tqdm

CLASS_PATTERN = r"\s*public class (?P<name>\w+) (?:extends (?P<parent>\w+) )?implements (?P<interface>\w+)\n"
ID_PATTERN = r"\s*public static const protocolId:uint = (?P<id>\d+);\n"
PUBLIC_VAR_PATTERN = r"\s*public var (?P<name>\w+):(?P<type>\S*)( = (?P<init>.*))?;\n"
VECTOR_TYPE_PATTERN = r"Vector\.<(?P<type>\w+)>"

ATTR_ASSIGN_PATTERN_OF_NAME = r"\s*this\.%s = (?:\w*)\.read(?P<type>\w*)\(\);\n"
VECTOR_ATTR_WRITE_PATTERN_OF_NAME = (
    r"\s*(?:\w*)\.write(?P<type>\w*)\(this\.%s\[(?:\w+)\]\);\n"
)
VECTOR_LEN_WRITE_PATTERN_OF_NAME = (
    r"\s*(?:\w*)\.write(?P<type>\w*)\(this\.%s\.length\);\n"
)
VECTOR_CONST_LEN_PATTERN_OF_NAME_AND_TYPE = (
    r"\s*this\.%s = new Vector\.<%s>\((?P<size>\d+),true\);\n"
)
DYNAMIC_TYPE_PATTERN_OF_TYPE = (
    r"\s*(?:this\.)?\w+ = ProtocolTypeManager\.getInstance\(%s,\w*\);\n"
)
OPTIONAL_VAR_PATTERN_OF_NAME = r"\s*if\(this\.%s == null\)\n"
HASH_FUNCTION_PATTERN = r"\s*HASH_FUNCTION\(data\);\n"
WRAPPED_BOOLEAN_PATTERN = r"\s*this.(?P<name>\w+) = BooleanByteWrapper\.getFlag\(.*;\n"


def parseVar(name: str, type_name: str, lines, types: dict):
    if type_name in ["Boolean", "ByteArray"]:
        return dict(name=name, length=None, type=type_name, optional=False)
    if type_name in types:
        _type = type_name

    _vector_matching = re.fullmatch(VECTOR_TYPE_PATTERN, type_name)
    if _vector_matching:
        return parseVectorVar(name, _vector_matching.group("type"), lines, types)

    attr_assign_pattern = ATTR_ASSIGN_PATTERN_OF_NAME % name
    dynamic_type_pattern = DYNAMIC_TYPE_PATTERN_OF_TYPE % type_name
    optional_var_pattern = OPTIONAL_VAR_PATTERN_OF_NAME % name

    optional = False

    for line in lines:
        _attr_matching = re.fullmatch(attr_assign_pattern, line)
        if _attr_matching:
            _type = _attr_matching.group("type")

        _dynamic_type_matching = re.fullmatch(dynamic_type_pattern, line)
        if _dynamic_type_matching:
            _type = False
            _extra_type = {'type': type_name, 'length': None}

        _optional_var_matching = re.fullmatch(optional_var_pattern, line)
        if _optional_var_matching:
            optional = True
    assert "_type" in locals()
    _var = {"name": name,
            "length": None,
            "type": _type,
            "optional": optional,
            }
    if '_extra_type' in locals():
        _var['extra_type'] = _extra_type

    return _var


def parseVectorVar(name, typename, lines, types: dict):
    if typename in types:
        _type = typename

    vector_attr_write_pattern = VECTOR_ATTR_WRITE_PATTERN_OF_NAME % name
    vector_len_write_pattern = VECTOR_LEN_WRITE_PATTERN_OF_NAME % name
    vector_const_len_pattern = VECTOR_CONST_LEN_PATTERN_OF_NAME_AND_TYPE % (
        name,
        typename,
    )
    dynamic_type_pattern = DYNAMIC_TYPE_PATTERN_OF_TYPE % typename

    for line in lines:
        _vector_attr_write_matching = re.fullmatch(vector_attr_write_pattern, line)
        if _vector_attr_write_matching:
            _type = _vector_attr_write_matching.group("type")

        _dynamic_type_matching = re.fullmatch(dynamic_type_pattern, line)
        if _dynamic_type_matching:
            _type = False
            _extra_type = {'type': typename, 'length': 'Short'}

        _vector_len_write_matching = re.fullmatch(vector_len_write_pattern, line)
        if _vector_len_write_matching:
            length = _vector_len_write_matching.group("type")

        _vector_const_len_matching = re.fullmatch(vector_const_len_pattern, line)
        if _vector_const_len_matching:
            length = int(_vector_const_len_matching.group("size"))
    assert "_type" in locals()
    assert "length" in locals()

    vector_var = {
        "name": name,
        "length": length,
        "type": _type,
        "optional": False,
    }
    if '_extra_type' in locals():
        vector_var['extra_type'] = _extra_type
    return vector_var


def generator_lines_from_path(_type):
    with _type["path"].open() as file:
        yield from file


def parse(_type: dict, msg_from_id: dict, types_from_id: dict, types: dict):
    vars = []
    hash_function = False
    wrapped_booleans = set()
    protocolId = None

    for line in generator_lines_from_path(_type):
        # iterate through line in file
        _class_matching = re.fullmatch(CLASS_PATTERN, line)
        if _class_matching:
            assert _class_matching.group("name") == _type["name"]
            parent = _class_matching.group("parent")
            if not parent in types:
                # check if parent is in interesting class
                parent = None
            _type["parent"] = parent

        _id_matching = re.fullmatch(ID_PATTERN, line)
        if _id_matching:
            protocolId = int(_id_matching.group("id"))

        _var_matching = re.fullmatch(PUBLIC_VAR_PATTERN, line)
        if _var_matching:
            var = parseVar(
                _var_matching.group("name"),
                _var_matching.group("type"),
                generator_lines_from_path(_type),
                types,
            )
            vars.append(var)

        _hash_function_matching = re.fullmatch(HASH_FUNCTION_PATTERN, line)
        if _hash_function_matching:
            hash_function = True

        _wrapped_boolean_matching = re.fullmatch(WRAPPED_BOOLEAN_PATTERN, line)
        if _wrapped_boolean_matching:
            wrapped_booleans.add(_wrapped_boolean_matching.group("name"))

    assert protocolId is not None
    _type["protocolId"] = protocolId

    # TODO Check if protocolId in protocolTypeManager ?
    if (
            "messages" in str(_type["path"])
            and _type["name"] != "AddTaxCollectorPresetSpellMessage"
    ):  # check if messages class
        assert protocolId not in msg_from_id
        msg_from_id[protocolId] = _type
    elif "types" in str(_type["path"]):  # check if types class
        assert protocolId not in types_from_id
        types_from_id[protocolId] = _type

    # separing boolvars and vars ?
    if sum(var["type"] == "Boolean" for var in vars) > 1:
        boolVars = [var for var in vars if var["name"] in wrapped_booleans]
        vars = [var for var in vars if var["name"] not in wrapped_booleans]
    else:
        boolVars = []

    _type["vars"] = vars
    _type["boolVars"] = boolVars
    _type["hash_function"] = hash_function
    _type["path"] = str(_type["path"])


def load_from_path(path, types: dict):
    """Put class message name with their path in types"""
    if isinstance(path, str):
        path = Path(path)
    for _path in path.glob("**/*.as"):
        name = _path.name[:-3]
        name_with_path = dict(name=name, path=_path)
        types[name] = name_with_path


if __name__ == "__main__":
    types = {}
    msg_from_id = {}
    types_from_id = {}

    paths = [
        os.path.join(
            Path(__file__).parent.parent.parent.parent,
            "resources",
            "code_source",
            "scripts",
            "com",
            "ankamagames",
            "dofus",
            "network",
            "types",
        ),
        os.path.join(
            Path(__file__).parent.parent.parent.parent,
            "resources",
            "code_source",
            "scripts",
            "com",
            "ankamagames",
            "dofus",
            "network",
            "messages",
        ),
    ]
    for _path in paths:
        load_from_path(_path, types)

    for _type in tqdm(types.values()):
        parse(_type, msg_from_id, types_from_id, types)

    types_with_path = deepcopy(types)
    for _type in types.values():
        if "path" in _type:
            del _type["path"]

    primitives = {
        _var["type"]
        for _type in types.values()
        for _var in _type["vars"]
        if _var["type"] and not _var["type"] in types
    }  # Get all types of data (UnsignedShort, UTF, VarUhInt etc...)

    with open(os.path.join(Path(__file__).parent, "protocol.pk"), "wb") as file:
        # write with pickle for better performance
        pickle.dump(types, file)
        pickle.dump(msg_from_id, file)
        pickle.dump(types_from_id, file)
        pickle.dump(primitives, file)

    with open(os.path.join(Path(__file__).parent, "protocol_type.json"), "w") as file:
        # write in json for human readable
        json.dump(types_with_path, file, indent=4)
