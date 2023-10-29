from enum import Enum


class UnpackMode(Enum):
    DEFAULT = 1
    SYNC = 2
    ASYNC = 3


class NetworkMessage:
    BIT_RIGHT_SHIFT_LEN_PACKET_ID = 2
    BIT_MASK = 3
