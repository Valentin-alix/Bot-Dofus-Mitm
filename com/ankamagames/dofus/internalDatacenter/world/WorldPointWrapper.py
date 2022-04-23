import com.ankamagames.atouin.managers.MapDisplayManager as mdm
from com.ankamagames.dofus.datacenter.world.MapPosition import MapPosition
from com.ankamagames.dofus.datacenter.world.MapScrollAction import MapScrollAction
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.types.positions.WorldPoint import WorldPoint

logger = Logger(__name__)


class WorldPointWrapper(WorldPoint):

    outdoorMapId: float

    _outdoorX: int

    _outdoorY: int

    _topNeighbourId: float = -1

    _bottomNeighbourId: float = -1

    _leftNeighbourId: float = -1

    _rightNeighbourId: float = -1

    def __init__(
        self,
        mapid: float,
        fixedOutdoor: bool = False,
        outdoorX: int = 0,
        outdoorY: int = 0,
    ):
        mapInfo: MapPosition = None
        super().__init__()
        self._mapId = mapid
        self.setFromMapId()
        if fixedOutdoor:
            self._outdoorX = outdoorX
            self._outdoorY = outdoorY
        else:
            mapInfo = MapPosition.getMapPositionById(mapid)
            if mapInfo:
                self._outdoorX = mapInfo.posX
                self._outdoorY = mapInfo.posY
            else:
                self._outdoorX = self.x
                self._outdoorY = self.y
        dmc = mdm.MapDisplayManager()
        if dmc and dmc.dataMap and dmc.dataMap.id == mapid:
            self._topNeighbourId = dmc.dataMap.topNeighbourId
            self._bottomNeighbourId = dmc.dataMap.bottomNeighbourId
            self._leftNeighbourId = dmc.dataMap.leftNeighbourId
            self._rightNeighbourId = dmc.dataMap.rightNeighbourId
        mapScrollaction: MapScrollAction = MapScrollAction.getMapScrollActionById(mapid)
        if mapScrollaction:
            if mapScrollaction.topExists:
                self._topNeighbourId = mapScrollaction.topMapId
            if mapScrollaction.bottomExists:
                self._bottomNeighbourId = mapScrollaction.bottomMapId
            if mapScrollaction.leftExists:
                self._leftNeighbourId = mapScrollaction.leftMapId
            if mapScrollaction.rightExists:
                self._rightNeighbourId = mapScrollaction.rightMapId

    @property
    def outdoorX(self) -> int:
        return self._outdoorX

    @property
    def outdoorY(self) -> int:
        return self._outdoorY

    @property
    def topNeighbourId(self) -> float:
        return self._topNeighbourId

    @property
    def bottomNeighbourId(self) -> float:
        return self._bottomNeighbourId

    @property
    def leftNeighbourId(self) -> float:
        return self._leftNeighbourId

    @property
    def rightNeighbourId(self) -> float:
        return self._rightNeighbourId

    def setOutdoorCoords(self, x: int, y: int) -> None:
        self._outdoorX = x
        self._outdoorY = y
