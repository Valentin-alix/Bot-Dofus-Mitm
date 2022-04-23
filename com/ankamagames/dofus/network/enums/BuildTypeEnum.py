from enum import Enum


class BuildTypeEnum(Enum):

    RELEASE: int = 0

    BETA: int = 1

    ALPHA: int = 2

    TESTING: int = 3

    INTERNAL: int = 4

    DEBUG: int = 5

    DRAFT: int = 6
