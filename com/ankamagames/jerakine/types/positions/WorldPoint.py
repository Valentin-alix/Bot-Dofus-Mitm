from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter
from com.ankamagames.jerakine.types.DataStoreType import JerakineError
from com.ankamagames.jerakine.types.positions.MapPoint import Point


class WorldPoint(IDataCenter):

    WORLD_ID_MAX: int = 2 << 12
    MAP_COORDS_MAX: int = 2 << 8

    def __init__(self):
        super().__init__()
        self._mapId: float = None
        self._worldId: int = None
        self._x: int = None
        self._y: int = None

    @classmethod
    def fromMapId(cls, mapId: float) -> "WorldPoint":
        wp = cls()
        wp._mapId = mapId
        wp.setFromMapId()
        return wp

    @classmethod
    def fromCoords(cls, worldId: int, x: int, y: int) -> "WorldPoint":
        wp = cls()
        wp._worldId = worldId
        wp._x = x
        wp._y = y
        wp.setFromCoords()
        return wp

    @property
    def mapId(self) -> float:
        return self._mapId

    @mapId.setter
    def mapId(self, mapId: float) -> None:
        self._mapId = mapId
        self.setFromMapId()

    @property
    def worldId(self) -> int:
        return self._worldId

    @worldId.setter
    def worldId(self, worldId: int) -> None:
        self._worldId = worldId
        self.setFromCoords()

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, x: int) -> None:
        self._x = x
        self.setFromCoords()

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, y: int) -> None:
        self._y = y
        self.setFromCoords()

    def add(self, offset: Point) -> None:
        self._x += offset.x
        self._y += offset.y
        self.setFromCoords()

    def setFromMapId(self) -> None:
        self._worldId = (self._mapId & 1073479680) >> 18
        self._x = self._mapId >> 9 & 511
        self._y = self._mapId & 511
        if (self._x & 256) == 256:
            self._x = -(self._x & 255)
        if (self._y & 256) == 256:
            self._y = -(self._y & 255)

    def setFromCoords(self) -> None:
        if (
            self._x > self.MAP_COORDS_MAX
            or self._y > self.MAP_COORDS_MAX
            or self._worldId > self.WORLD_ID_MAX
        ):
            raise JerakineError("Coordinates or world identifier out of range.")
        worldValue: int = self._worldId & 4095
        xValue: int = abs(self._x) & 255
        if self._x < 0:
            xValue |= 256
        yValue: int = abs(self._y) & 255
        if self._y < 0:
            yValue |= 256
        self._mapId = worldValue << 18 | (xValue << 9 | yValue)
