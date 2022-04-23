import math

from com.ankamagames.jerakine.types.enums.DirectionsEnum import DirectionsEnum


class Point:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"


class MapPoint:
    RIGHT = 0
    DOWN_RIGHT = 1
    DOWN = 2
    DOWN_LEFT = 3
    LEFT = 4
    UP_LEFT = 5
    UP = 6
    UP_RIGHT = 7
    MAP_WIDTH = 14
    MAP_HEIGHT = 20
    CELLPOS = dict[int, Point]()
    VECTOR_RIGHT = Point(1, 1)
    VECTOR_DOWN_RIGHT = Point(1, 0)
    VECTOR_DOWN = Point(1, -1)
    VECTOR_DOWN_LEFT = Point(0, -1)
    VECTOR_LEFT = Point(-1, -1)
    VECTOR_UP_LEFT = Point(-1, 0)
    VECTOR_UP = Point(-1, 1)
    VECTOR_UP_RIGHT = Point(0, 1)
    _bInit = False

    def __init__(self, cellId=None, x=None, y=None) -> None:
        self._bInit = True
        self._nCellId = cellId
        self._nX = x
        self._nY = y

    def setFromCellId(self):
        if not MapPoint._bInit:
            MapPoint.init()
        p = self.CELLPOS[self._nCellId]
        self._nX = p.x
        self._nY = p.y

    def setFromCoords(self):
        if not MapPoint._bInit:
            MapPoint.init()
        self._nCellId = (
            (self._nX - self._nY) * MapPoint.MAP_WIDTH
            + self._nY
            + (self._nX - self._nY) // 2
        )

    @classmethod
    def fromCellId(cls, cellId: int):
        mp = cls(cellId)
        mp.setFromCellId()
        return mp

    @classmethod
    def fromCoords(cls, x: int, y: int):
        mp = cls()
        mp._nX = x
        mp._nY = y
        mp.setFromCoords()
        return mp

    @staticmethod
    def getOrientationsDistance(i1: int, i2: int) -> int:
        return min(abs(i2 - i1), abs(8 - i2 + i1))

    @staticmethod
    def isInMap(i1: int, i2: int):
        return (
            i1 + i2 >= 0
            and i1 - i2 >= 0
            and i1 - i2 < MapPoint.MAP_HEIGHT * 2
            and i1 + i2 < MapPoint.MAP_WIDTH * 2
        )

    @classmethod
    def init(cls):
        cls._bInit = True
        i1 = 0
        i2 = 0
        i3 = 0
        for _ in range(cls.MAP_HEIGHT):
            for j in range(cls.MAP_WIDTH):
                cls.CELLPOS[i3] = Point(i1 + j, i2 + j)
                i3 += 1
            i1 += 1
            for j in range(cls.MAP_WIDTH):
                cls.CELLPOS[i3] = Point(i1 + j, i2 + j)
                i3 += 1
            i2 -= 1

    @property
    def cellId(self) -> int:
        return self._nCellId

    @cellId.setter
    def cellId(self, i: int):
        if not type(i) == int:
            raise TypeError("cellId must be an int")
        self._nCellId = i
        self.setFromCellId()

    @property
    def x(self) -> int:
        return self._nX

    @x.setter
    def x(self, i: int):
        self._nX = i
        self.setFromCoords()

    @property
    def y(self) -> int:
        return self._nY

    @y.setter
    def y(self, i: int):
        self._nY = i
        self.setFromCoords()

    def getCoordinates(self) -> Point:
        return Point(self._nX, self._nY)

    def distanceTo(self, mp: "MapPoint") -> int:
        return math.sqrt((self.y - mp.y) ** 2 + (self.y - mp.y) ** 2)

    def distanceToCell(self, mp: "MapPoint"):
        return abs(self.y - mp.y) + abs(self.y - mp.y)

    def orientationTo(self, mp: "MapPoint") -> DirectionsEnum:
        if self._nX == mp._nX and self._nY == mp._nY:
            return DirectionsEnum.DOWN_RIGHT
        p = Point()
        p.x = 1 if mp._nX > self._nX else (-1 if mp._nX < self._nX else 0)
        p.y = 1 if mp._nY > self._nY else (-1 if mp._nY < self._nY else 0)
        nb = DirectionsEnum.RIGHT
        if p.x == self.VECTOR_RIGHT.x and p.y == self.VECTOR_RIGHT.y:
            nb = DirectionsEnum.RIGHT

        elif p.x == self.VECTOR_DOWN_RIGHT.x and p.y == self.VECTOR_DOWN_RIGHT.y:
            nb = DirectionsEnum.DOWN_RIGHT

        elif p.x == self.VECTOR_DOWN.x and p.y == self.VECTOR_DOWN.y:
            nb = DirectionsEnum.DOWN

        elif p.x == self.VECTOR_DOWN_LEFT.x and p.y == self.VECTOR_DOWN_LEFT.y:
            nb = DirectionsEnum.DOWN_LEFT

        elif p.x == self.VECTOR_LEFT.x and p.y == self.VECTOR_LEFT.y:
            nb = DirectionsEnum.LEFT

        elif p.x == self.VECTOR_UP_LEFT.x and p.y == self.VECTOR_UP_LEFT.y:
            nb = DirectionsEnum.UP_LEFT

        elif p.x == self.VECTOR_UP.x and p.y == self.VECTOR_UP.y:
            nb = DirectionsEnum.UP

        elif p.x == self.VECTOR_UP_RIGHT.x and p.y == self.VECTOR_UP_RIGHT.y:
            nb = DirectionsEnum.UP_RIGHT
        return nb

    def advancedOrientationTo(self, mp: "MapPoint", b: bool) -> int:
        if mp == None:
            return 0
        i1 = mp.x - self.x
        i2 = self.y - mp.y
        i3 = (
            math.acos(i1 / math.sqrt(math.pow(i1, 2) + math.pow(i2, 2)))
            * 180
            / math.pi
            * (-1 if mp.y > self.y else 1)
        )
        if b:
            i3 = round(i3 / 90) * 2 + 1
        else:
            i3 = round(i3 / 45) + 1
        if i3 < 0:
            i3 += 8
        return i3

    def pointSymetry(self, mp: "MapPoint") -> "MapPoint":
        i1 = 2 * mp.x - self.x
        i2 = 2 * mp.y - self.y
        if self.isInMap(i1, i2):
            return MapPoint.fromCoords(i1, i2)
        return None

    def __eq__(self, mp: "MapPoint") -> bool:
        return self._nCellId == mp._nCellId

    def __str__(self):
        return f"MapPoint(x: {self.x}, y: {self.y}, id: {self.cellId})"

    def __hash__(self) -> int:
        return self._nCellId
