from enum import Enum


class GameServerTypeEnum(Enum):
    SERVER_TYPE_UNDEFINED: int = -1

    SERVER_TYPE_CLASSICAL: int = 0

    SERVER_TYPE_HARDCORE: int = 1

    SERVER_TYPE_KOLIZEUM: int = 2

    SERVER_TYPE_TOURNAMENT: int = 3

    SERVER_TYPE_EPIC: int = 4

    SERVER_TYPE_TEMPORIS: int = 5
