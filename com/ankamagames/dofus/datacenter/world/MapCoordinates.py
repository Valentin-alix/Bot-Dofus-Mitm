from com.ankamagames.dofus.datacenter.world.MapPosition import MapPosition
from com.ankamagames.jerakine.data.GameData import GameData
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter
from com.ankamagames.jerakine.logger.Logger import Logger


logger = Logger(__name__)


class MapCoordinates(IDataCenter):

    MODULE: str = "MapCoordinates"

    UNDEFINED_COORD: int = int.MIN_VALUE

    compressedCoords: int

    mapIds: list[float]

    _x: int = -2147483648

    _y: int = -2147483648

    _maps: list[MapPosition]

    def __init__(self):
        super().__init__()

    @classmethod
    def getMapCoordinatesByCompressedCoords(
        cls, compressedCoords: int
    ) -> "MapCoordinates":
        return GameData.getObject(cls.MODULE, compressedCoords)

    @classmethod
    def getMapCoordinatesByCoords(cls, x: int, y: int) -> "MapCoordinates":
        xCompressed: int = cls.getCompressedValue(x)
        yCompressed: int = cls.getCompressedValue(y)
        return cls.getMapCoordinatesByCompressedCoords(
            (xCompressed << 16) + yCompressed
        )

    @classmethod
    def getSignedValue(cls, v: int) -> int:
        isNegative = (v & 32768) > 0
        TrueValue = v & 32767
        return int(0 - TrueValue) if not isNegative else int(TrueValue)

    @staticmethod
    def getCompressedValue(v: int) -> int:
        return int(32768 | v & 32767) if v < 0 else int(v & 32767)

    @property
    def x(self) -> int:
        if self._x == self.UNDEFINED_COORD:
            self._x = self.getSignedValue((self.compressedCoords & 4294901760) >> 16)
        return self._x

    @property
    def y(self) -> int:
        if self._y == self.UNDEFINED_COORD:
            self._y = self.getSignedValue(self.compressedCoords & 65535)
        return self._y

    @property
    def maps(self) -> list[MapPosition]:
        i: int = 0
        if not self._maps:
            self._maps = len(list[MapPosition](self.mapIds), True)
            for i in range(len(self.mapIds)):
                self._maps[i] = MapPosition.getMapPositionById(self.mapIds[i])
        return self._maps
