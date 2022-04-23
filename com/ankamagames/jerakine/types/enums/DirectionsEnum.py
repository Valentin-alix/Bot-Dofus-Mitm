from enum import Enum


class DirectionsEnum(Enum):
    RIGHT: int = 0

    DOWN_RIGHT: int = 1

    DOWN: int = 2

    DOWN_LEFT: int = 3

    LEFT: int = 4

    UP_LEFT: int = 5

    UP: int = 6

    UP_RIGHT: int = 7

    @classmethod
    def getMapChangeDirections(cls):
        return [cls.RIGHT, cls.DOWN, cls.LEFT, cls.UP]
