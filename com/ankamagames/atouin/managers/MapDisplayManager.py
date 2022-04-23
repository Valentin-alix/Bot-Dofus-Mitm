from com.ankamagames.atouin.messages.MapLoadedMessage import MapLoadedMessage
from com.ankamagames.jerakine.logger.Logger import Logger
from time import perf_counter
import com.ankamagames.atouin.utils.DataMapProvider as dmpm
from com.ankamagames.jerakine.metaclasses.Singleton import Singleton
from com.ankamagames.jerakine.types.positions.WorldPoint import WorldPoint

logger = Logger(__name__)


class MapDisplayManager(metaclass=Singleton):

    MEMORY_LOG: dict = dict()
    _currentMap: WorldPoint
    _mapInstanceId: float = 0
    _lastMap: WorldPoint
    _nMapLoadStart: int
    _nMapLoadEnd: int

    def __init__(self) -> None:
        from com.ankamagames.jerakine.resources.loaders.MapLoader import MapLoader

        self._loader = MapLoader()
        self._currentMap = None
        self.currentDataMap = None
        self._lastMap = None
        self._nMapLoadStart = 0
        self._nMapLoadEnd = 0
        self._forceReloadWithoutCache = False

    @property
    def dataMap(self):
        return self.currentDataMap

    @property
    def currentMapPoint(self) -> WorldPoint:
        return self._currentMap

    @property
    def mapInstanceId(self) -> float:
        return self._mapInstanceId

    @mapInstanceId.setter
    def mapInstanceId(self, mapId: float) -> None:
        self._mapInstanceId = mapId

    def reset(self) -> None:
        self._currentMap = None
        logger.debug("mapInstanceId reset 0")
        self._mapInstanceId = 0
        self._lastMap = None

    def mapDisplayed(self) -> None:
        InteractiveCellManager().updateInteractiveCell(self.currentDataMap)

    def loadMap(self, mapId: int, forceReloadWithoutCache: bool = False) -> None:
        from com.ankamagames.dofus.kernel.Kernel import Kernel

        self.lastDataMap = self.currentDataMap
        self._forceReloadWithoutCache = forceReloadWithoutCache
        self._nMapLoadStart = perf_counter()
        map = self._loader.load(mapId)
        self._nMapLoadEnd = perf_counter()
        logger.debug(
            "Map loaded in " + str(self._nMapLoadEnd - self._nMapLoadStart) + " seconds"
        )
        dmpm.DataMapProvider().resetUpdatedCell()
        dmpm.DataMapProvider().resetSpecialEffects()
        self.currentDataMap = map
        self._currentMap = WorldPoint.fromMapId(map.id)
        msg = MapLoadedMessage()
        msg.id = self._currentMap.mapId
        Kernel().getWorker().process(msg)
