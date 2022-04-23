from functools import reduce
import importlib
import json
import random
import sys
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.network.CustomDataWrapper import ByteArray
import com.ankamagames.jerakine.network.NetworkMessage as bnm
from com.ankamagames.jerakine.network.parser.TypeEnum import TypeEnum
from com.ankamagames.jerakine.network.parser.ProtocolSpec import D2PROTOCOL

logger = Logger(__name__)
dataWrite = {
    name: (getattr(ByteArray, "read" + name), getattr(ByteArray, "write" + name))
    for name in D2PROTOCOL["primitives"]
}

PY_PRIMITIVES = {int, float, str, bool}


class NetworkMessageEncoder:
    @classmethod
    def encode(
        cls, inst: "bnm.NetworkMessage", data=None, random_hash=True
    ) -> ByteArray:
        spec = inst.getSpec()
        try:
            return cls._encode(spec, inst, data, random_hash)
        except:
            logger.error("Error while encoding %s", inst.__dict__)
            raise

    @classmethod
    def jsonEncode(cls, inst: "bnm.NetworkMessage", random_hash=True) -> dict:
        spec = inst.getSpec()
        return cls._jsonEncode(spec, inst, random_hash)

    @classmethod
    def _encode(cls, spec: dict, inst, data=None, random_hash=True) -> ByteArray:
        if data is None:
            data = ByteArray()

        if spec.get("dynamicType"):
            msg_type = D2PROTOCOL["type"][spec["name"]]
            data.writeUnsignedShort(msg_type["protocolId"])

        typeId = spec.get("typeId")
        if typeId is not None and TypeEnum(typeId) != TypeEnum.OBJECT:
            try:
                dataWrite[spec["type"]][1](data, inst)
            except:
                logger.error("Error while writing %s", inst)
                raise
            return data

        parent = spec.get("parent")
        if parent is not None:
            cls._encode(D2PROTOCOL["type"][parent], inst, data)

        if "fields" not in spec:
            spec = D2PROTOCOL["type"][spec["type"]]

        cls.writeBooleans(spec["boolfields"], inst, data)

        for field in spec["fields"]:

            if field["optional"]:
                if (
                    hasattr(inst, field["name"])
                    and getattr(inst, field["name"]) is not None
                ):
                    data.writeByte(1)

                else:
                    data.writeByte(0)
                    continue

            if field["length"] is not None or field.get("lengthTypeId") is not None:
                cls.writeArray(field, getattr(inst, field["name"]), data)

            else:
                try:
                    cls._encode(field, getattr(inst, field["name"]), data)
                except:
                    logger.error("Error while writing %s", field)
                    raise

        if hasattr(inst, "hash_function"):
            data.write(getattr(inst, "hash_function"))

        elif spec["hash_function"] and random_hash:
            hash = bytes(random.getrandbits(8) for _ in range(48))
            data.write(hash)

        return data

    @classmethod
    def writeBooleans(cls, boolfields, inst, data: ByteArray):
        bits = []
        for var in boolfields:
            bits.append(getattr(inst, var["name"]))
            if len(bits) == 8:
                data.writeByte(reduce(lambda a, b: 2 * a + b, bits[::-1]))
                bits = []
        if bits:
            data.writeByte(reduce(lambda a, b: 2 * a + b, bits[::-1]))

    @classmethod
    def writeArray(cls, var, inst, data):
        n = len(inst)
        if var["length"] is not None:
            assert n == var["length"]

        elif var["lengthTypeId"] is not None:
            primitiveName = TypeEnum.getPrimitiveName(TypeEnum(var["lengthTypeId"]))
            dataWrite[primitiveName][1](data, n)

        if var["type"] in D2PROTOCOL["primitives"]:
            for it in inst:
                dataWrite[var["type"]][1](data, it)

        else:
            for it in inst:
                cls._encode(D2PROTOCOL["type"][var["name"]], it, data)

    @classmethod
    def isVector(cls, var):
        return var["length"] is not None or var.get("lengthTypeId") is not None

    @classmethod
    def isPrimitive(cls, var):
        return var["type"] in D2PROTOCOL["primitives"]

    @classmethod
    def isDynamicType(cls, field):
        return field.get("dynamicType")

    @classmethod
    def _jsonEncode(cls, spec: dict, inst, random_hash=True) -> dict:
        ans = {"__type__": inst.__class__.__name__}

        parent = spec.get("parent")
        if parent is not None:
            ans.update(cls._jsonEncode(D2PROTOCOL["type"][parent], inst))

        for bfield in spec["boolfields"]:
            ans[bfield["name"]] = getattr(inst, bfield["name"])

        for field in spec["fields"]:
            fname = field["name"]
            if field["optional"] and not hasattr(inst, fname):
                continue
            attr = getattr(inst, fname)
            if type(attr) is list:
                if len(attr) == 0:
                    ans[fname] = []
                    continue
                if type(attr[0]) in PY_PRIMITIVES:
                    ans[fname] = attr
                else:
                    ans[fname] = [cls.jsonEncode(it) for it in attr]
            elif type(attr) in PY_PRIMITIVES:
                ans[fname] = attr
            else:
                ans[fname] = cls.jsonEncode(attr)

        if hasattr(inst, "hash_function"):
            ans["hash_function"] = getattr(inst, "hash_function")

        elif spec["hash_function"] and random_hash:
            hash = bytes(random.getrandbits(8) for _ in range(48))
            ans["hash_function"] = hash

        return ans

    @classmethod
    def decodeFromJson(cls, json: dict) -> "bnm.NetworkMessage":
        className = json["__type__"]
        classSpec = D2PROTOCOL["type"][className]
        modulePath = classSpec["package"]
        clsModule = classSpec["package"]
        try:
            clsModule = sys.modules[modulePath]
        except:
            clsModule = importlib.import_module(modulePath)
        objClass = getattr(clsModule, className)
        instance = objClass()
        bnm.NetworkMessage.__init__(instance)
        for k, v in json.items():
            if k == "__type__":
                continue
            if type(v) is dict:
                setattr(instance, k, cls.decodeFromJson(v))

            elif type(v) is list:

                if len(v) == 0:
                    setattr(instance, k, [])
                    continue

                if type(v[0]) in PY_PRIMITIVES:
                    setattr(instance, k, v)

                else:
                    setattr(instance, k, [cls.decodeFromJson(it) for it in v])

            else:
                setattr(instance, k, v)

        return instance
