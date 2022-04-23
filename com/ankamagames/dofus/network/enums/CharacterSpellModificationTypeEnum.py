from enum import Enum


class CharacterSpellModificationTypeEnum(Enum):

    INVALID_MODIFICATION: int = 0

    RANGEABLE: int = 1

    DAMAGE: int = 2

    BASE_DAMAGE: int = 3

    HEAL_BONUS: int = 4

    AP_COST: int = 5

    CAST_INTERVAL: int = 6

    CAST_INTERVAL_SET: int = 7

    CRITICAL_HIT_BONUS: int = 8

    CAST_LINE: int = 9

    LOS: int = 10

    MAX_CAST_PER_TURN: int = 11

    MAX_CAST_PER_TARGET: int = 12

    RANGE_MAX: int = 13

    RANGE_MIN: int = 14
