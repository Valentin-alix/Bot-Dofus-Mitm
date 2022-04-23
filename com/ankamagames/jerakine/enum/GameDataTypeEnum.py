from ast import Bytes
from ctypes.wintypes import BYTE
from pickle import BYTEARRAY8


class GameDataTypeEnum:

    INT: int = -1
    BOOLEAN: int = -2
    STRING: int = -3
    NUMBER: int = -4
    I18N: int = -5
    UINT: int = -6
    VECTOR: int = -99
