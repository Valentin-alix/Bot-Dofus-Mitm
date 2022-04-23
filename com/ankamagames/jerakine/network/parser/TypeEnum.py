from enum import Enum


class TypeEnum(Enum):
    VARLONG = 13
    UTF = 2
    VARSHORT = 14
    UNSIGNEDBYTE = 3
    VARUHSHORT = 9
    VARINT = 5
    UNSIGNEDSHORT = 16
    VARUHLONG = 7
    BOOLEAN = 8
    FLOAT = 4
    UNSIGNEDINT = 10
    DOUBLE = 11
    VARUHINT = 12
    INT = 1
    BYTE = 0
    BYTEARRAY = 15
    SHORT = 6
    OBJECT = -1

    @staticmethod
    def getPrimitiveName(type: "TypeEnum"):
        matcher = {
            TypeEnum.INT: "Int",
            TypeEnum.UNSIGNEDINT: "UnsignedInt",
            TypeEnum.SHORT: "Short",
            TypeEnum.UNSIGNEDSHORT: "UnsignedShort",
            TypeEnum.BYTE: "Byte",
            TypeEnum.UNSIGNEDBYTE: "UnsignedByte",
            TypeEnum.FLOAT: "Float",
            TypeEnum.DOUBLE: "Double",
            TypeEnum.BOOLEAN: "bool",
            TypeEnum.VARINT: "VarInt",
            TypeEnum.VARLONG: "VarLong",
            TypeEnum.UTF: "UTF",
            TypeEnum.VARUHSHORT: "VarUhShort",
            TypeEnum.VARUHINT: "VarUhInt",
            TypeEnum.VARSHORT: "VarShort",
            TypeEnum.VARUHLONG: "VarUhLong",
        }
        return matcher.get(type)

    @classmethod
    def fromString(cls, string):
        try:
            return getattr(cls, string.upper())
        except:
            return cls.OBJECT
