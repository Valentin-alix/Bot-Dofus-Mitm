import logging
import random
from functools import reduce

from app.interfaces.models.network.data import Data
from app.network.protocol.protocol_load import primitives, types, types_from_id

logger = logging.getLogger("labot")

primitives = {
    name: (getattr(Data, "read" + name), getattr(Data, "write" + name))
    for name in primitives
}


def readBooleans(boolean_vars, data):
    ans = {}
    bvars = iter(boolean_vars)
    for _ in range(0, len(boolean_vars), 8):
        bits = format(data.readByte(), "08b")[::-1]
        for val, var in zip(bits, bvars):
            # be careful, you have to
            # put bits first in zip
            ans[var["name"]] = val == "1"
    return ans


def readVec(var, data):
    assert var["length"] is not None
    if isinstance(var["length"], int):
        length: int = var["length"]
    else:
        length = read(var["length"], data)
    ans = []
    for _ in range(length):
        ans.append(read(var["type"], data))
    return ans


def read(_type, data: Data):
    if _type is False:
        _type = types_from_id[data.readUnsignedShort()]
    elif isinstance(_type, str):
        if _type in primitives:
            return primitives[_type][0](data)
        _type = types[_type]
    logger.debug("reading data %s", data)
    logger.debug("with type %s", _type)

    if _type["parent"] is not None:
        logger.debug("calling parent %s", _type["parent"])
        ans = read(_type["parent"], data)
        ans["__type__"] = _type["name"]
    else:
        ans = {"__type__": _type["name"]}

    logger.debug("reading boolean variables")
    ans.update(readBooleans(_type["boolVars"], data))
    logger.debug("remaining data: %s", data.data[data.pos :])

    for var in _type["vars"]:
        logger.debug("reading %s", var)
        if var["optional"]:
            if not data.readByte():
                continue
        if var["length"] is not None:
            ans[var["name"]] = readVec(var, data)
        else:
            ans[var["name"]] = read(var["type"], data)
        logger.debug("remaining data: %s", data.data[data.pos :])
    if _type["hash_function"] and data.remaining() == 48:
        ans["hash_function"] = data.read(48)
    return ans


def writeBooleans(bool_vars, values: dict, data: Data):
    bits = []
    for bool_var in bool_vars:
        bits.append(values[bool_var["name"]])
        if len(bits) == 8:
            data.writeByte(reduce(lambda a, b: 2 * a + b, bits[::-1]))
            bits = []
    if bits:
        data.writeByte(reduce(lambda a, b: 2 * a + b, bits[::-1]))


def writeVec(var, values: dict, data: Data):
    assert var["length"] is not None
    n = len(values)
    if isinstance(var["length"], int):
        assert n == var["length"]
    else:
        write(var["length"], n, data)
    for it in values:
        write(var["type"], it, data)


def write(_type, _json: dict, data: Data | None = None, random_hash=True) -> Data:
    if data is None:
        data = Data()
    if _type is False:
        _type = types[_json["__type__"]]
        data.writeUnsignedShort(_type["protocolId"])
    elif isinstance(_type, str):
        if _type in primitives:
            primitives[_type][1](data, _json)
            return data
        _type = types[_type]

    parent = _type["parent"]
    if parent is not None:
        write(parent, _json, data, random_hash)

    writeBooleans(_type["boolVars"], _json, data)
    for var in _type["vars"]:
        if var["optional"]:
            if var["name"] in _json:
                data.writeByte(1)
            else:
                data.writeByte(0)
                continue

        if var["length"] is not None:
            writeVec(var, _json[var["name"]], data)
        else:
            write(var["type"], _json[var["name"]], data)

    if "hash_function" in _json:
        data.write(_json["hash_function"])
    elif _type["hash_function"] and random_hash:
        _hash = bytes(random.getrandbits(8) for _ in range(48))
        data.write(_hash)

    return data
