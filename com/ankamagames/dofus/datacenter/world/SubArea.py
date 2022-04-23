from com.ankamagames.dofus.datacenter.world.Area import Area
from com.ankamagames.dofus.datacenter.world.MapPosition import MapPosition
from com.ankamagames.dofus.datacenter.world.WorldMap import WorldMap
from com.ankamagames.dofus.types.IdAccessors import IdAccessors
from com.ankamagames.jerakine.data.GameData import GameData
from com.ankamagames.jerakine.data.I18n import I18n
from com.ankamagames.jerakine.data.IposInit import IPostInit
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter
from com.ankamagames.jerakine.types.positions.MapPoint import Point
from flash.geom.Rectangle import Rectangle


class SubArea(IDataCenter, IPostInit):

    MODULE: str = "SubAreas"

    def __init__(self):
        self._allSubAreas = list[SubArea]()

        self.id: int = None

        self.nameId: int = None

        self.areaId: int = None

        self.playlists = list[list[int]]()

        self.mapIds = list[float]()

        self.bounds: Rectangle = None

        self.shape = list[int]()

        self.worldmapId: int = None

        self.customWorldMap = list[int]()

        self.packId: int = None

        self.level: int = None

        self.isConquestVillage: bool = None

        self.basicAccountAllowed: bool = None

        self.displayOnWorldMap: bool = None

        self.mountAutoTripAllowed: bool = None

        self.psiAllowed: bool = None

        self.monsters = list[int]()

        self.capturable: bool = None

        self.quests = list[list[float]]()

        self.npcs = list[list[float]]()

        self.harvestables = list[int]()

        self.associatedZaapMapId: int = None

        self._name: str = None

        self._undiatricalName: str = None

        self._area: Area = None

        self._worldMap: WorldMap = None

        self._center: Point = None

        self._zaapMapCoord: MapPosition = None
        super().__init__()

    @staticmethod
    def getSubAreaById(id: int) -> "SubArea":
        subArea: SubArea = GameData.getObject(SubArea.MODULE, id)
        if not subArea or not subArea.area:
            return None
        return subArea

    @staticmethod
    def getSubAreaByMapId(mapId: float) -> "SubArea":
        mp: MapPosition = MapPosition.getMapPositionById(mapId)
        if mp:
            return mp.subArea
        return None

    @classmethod
    def getAllSubArea(cls) -> list:
        if cls._allSubAreas:
            return cls._allSubAreas
        _allSubAreas = GameData.getobjects(cls.MODULE)
        return _allSubAreas

    idAccessors: IdAccessors = IdAccessors(getSubAreaById, getAllSubArea)

    @property
    def name(self) -> str:
        if not self._name:
            self._name = I18n.getText(self.nameId)
        return self._name

    @property
    def undiatricalName(self) -> str:
        if not self._undiatricalName:
            self._undiatricalName = I18n.getUnDiacriticalText(self.nameId)
        return self._undiatricalName

    @property
    def area(self) -> Area:
        if not self._area:
            self._area = Area.getAreaById(self.areaId)
        return self._area

    @property
    def worldmap(self) -> WorldMap:
        if not self._worldMap:
            if self.hasCustomWorldMap:
                self._worldMap = WorldMap.getWorldMapById(self.customWorldMap[0])
            else:
                self._worldMap = self.area.worldmap
        return self._worldMap

    @property
    def hasCustomWorldMap(self) -> bool:
        return self.customWorldMap and len(self.customWorldMap) > 0

    @property
    def center(self) -> Point:
        minX: int = 0
        maxX: int = 0
        minY: int = 0
        maxY: int = 0
        i: int = 0
        posX: int = 0
        posY: int = 0
        nCoords: int = len(self.shape)
        if not self._center and nCoords > 0:
            posX = self.shape[0]
            posY = self.shape[1]
            minX = maxX = int(posX - 11000) if posX > 10000 else int(posX)
            minY = maxY = int(posY - 11000) if posY > 10000 else int(posY)
            for i in range(nCoords):
                posX = self.shape[i]
                posY = self.shape[i + 1]
                if posX > 10000:
                    posX -= 11000
                if posY > 10000:
                    posY -= 11000
                minX = int(posX) if posX < minX else int(minX)
                maxX = int(posX) if posX > maxX else int(maxX)
                minY = int(posY) if posY < minY else int(minY)
                maxY = int(posY) if posY > maxY else int(maxY)
            self._center = Point((minX + maxX) / 2, (minY + maxY) / 2)
        return self._center

    @property
    def zaapMapPosition(self) -> MapPosition:
        if not self._zaapMapCoord:
            self._zaapMapCoord = MapPosition.getMapPositionById(
                self.associatedZaapMapId
            )
        return self._zaapMapCoord

    def postInit(self) -> None:
        self.name
        self.undiatricalName
