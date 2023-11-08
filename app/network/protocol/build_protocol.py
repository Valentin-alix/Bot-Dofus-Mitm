import os
import pickle
import re
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


def load_from_path(path):
    if isinstance(path, str):
        path = Path(path)
    for p in path.glob("**/*.as"):
        name = p.name[:-3]
        new = dict(name=name, path=p)
        types[name] = new


def lines(_type):
    with _type["path"].open() as file:
        yield from file


def parseVar(name, typename, lines):
    if typename in ["Boolean", "ByteArray"]:
        return dict(name=name, length=None, type=typename, optional=False)
    if typename in types:
        type = typename

    m = re.fullmatch(VECTOR_TYPE_PATTERN, typename)
    if m:
        return parseVectorVar(name, m.group("type"), lines)

    attr_assign_pattern = ATTR_ASSIGN_PATTERN_OF_NAME % name
    dynamic_type_pattern = DYNAMIC_TYPE_PATTERN_OF_TYPE % typename
    optional_var_pattern = OPTIONAL_VAR_PATTERN_OF_NAME % name

    optional = False

    for line in lines:
        m = re.fullmatch(attr_assign_pattern, line)
        if m:
            type = m.group("type")

        m = re.fullmatch(dynamic_type_pattern, line)
        if m:
            type = False

        m = re.fullmatch(optional_var_pattern, line)
        if m:
            optional = True

    return dict(name=name, length=None, type=type, optional=optional)


def parseVectorVar(name, typename, lines):
    if typename in types:
        type = typename

    vector_attr_write_pattern = VECTOR_ATTR_WRITE_PATTERN_OF_NAME % name
    vector_len_write_pattern = VECTOR_LEN_WRITE_PATTERN_OF_NAME % name
    vector_const_len_pattern = VECTOR_CONST_LEN_PATTERN_OF_NAME_AND_TYPE % (
        name,
        typename,
    )
    dynamic_type_pattern = DYNAMIC_TYPE_PATTERN_OF_TYPE % typename

    for line in lines:
        m = re.fullmatch(vector_attr_write_pattern, line)
        if m:
            type = m.group("type")

        m = re.fullmatch(dynamic_type_pattern, line)
        if m:
            type = False

        m = re.fullmatch(vector_len_write_pattern, line)
        if m:
            length = m.group("type")

        m = re.fullmatch(vector_const_len_pattern, line)
        if m:
            length = int(m.group("size"))

    return dict(name=name, length=length, type=type, optional=False)


def parse(t):
    vars = []
    hash_function = False
    wrapped_booleans = set()

    for line in lines(t):
        m = re.fullmatch(CLASS_PATTERN, line)
        if m:
            assert m.group("name") == t["name"]
            parent = m.group("parent")
            if not parent in types:
                parent = None
            t["parent"] = parent

        m = re.fullmatch(ID_PATTERN, line)
        if m:
            protocolId = int(m.group("id"))

        m = re.fullmatch(PUBLIC_VAR_PATTERN, line)
        if m:
            var = parseVar(m.group("name"), m.group("type"), lines(t))
            vars.append(var)

        m = re.fullmatch(HASH_FUNCTION_PATTERN, line)
        if m:
            hash_function = True

        m = re.fullmatch(WRAPPED_BOOLEAN_PATTERN, line)
        if m:
            wrapped_booleans.add(m.group("name"))

    t["protocolId"] = protocolId

    if "messages" in str(t["path"]):
        # assert protocolId not in msg_from_id
        msg_from_id[protocolId] = t
    elif "types" in str(t["path"]):
        # assert protocolId not in types_from_id
        types_from_id[protocolId] = t

    if sum(var["type"] == "Boolean" for var in vars) > 1:
        boolVars = [var for var in vars if var["name"] in wrapped_booleans]
        vars = [var for var in vars if var["name"] not in wrapped_booleans]
    else:
        boolVars = []

    t["vars"] = vars
    t["boolVars"] = boolVars
    t["hash_function"] = hash_function
    del t["path"]


def build():
    for t in tqdm(types.values()):
        parse(t)


if __name__ == "__main__":
    types = {}
    msg_from_id = {}
    types_from_id = {}

    paths = [
        os.path.join(
            Path(__file__).parent.parent.parent.parent,
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
            "code_source",
            "scripts",
            "com",
            "ankamagames",
            "dofus",
            "network",
            "messages",
        ),
    ]
    print(paths)
    for p in paths:
        load_from_path(p)

    primitives = {
        v["type"]
        for t in types.values()
        for v in t["vars"]
        if v["type"] and not v["type"] in types
    }

    with open(os.path.join(Path(__file__).parent, "protocol.pk"), "wb") as f:
        pickle.dump(types, f)
        pickle.dump(msg_from_id, f)
        pickle.dump(types_from_id, f)
        pickle.dump(primitives, f)
