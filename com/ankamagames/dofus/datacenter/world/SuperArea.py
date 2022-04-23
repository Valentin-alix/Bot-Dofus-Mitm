from com.ankamagames.dofus.datacenter.world.WorldMap import WorldMap
from com.ankamagames.dofus.types.IdAccessors import IdAccessors
from com.ankamagames.jerakine.data.GameData import GameData
from com.ankamagames.jerakine.data.I18n import I18n
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter


class SuperArea(IDataCenter):

    MODULE: str = "SuperAreas"

    _allSuperAreas = list()

    def __init__(self):
        self._worldmap = None
        self._name = None
        self.worldmapId: int = None
        self.nameId: int = None
        self.id: int = None

        super().__init__()

    @staticmethod
    def getSuperAreaById(id: int) -> "SuperArea":
        superArea: SuperArea = GameData.getObject(SuperArea.MODULE, id)
        if not superArea:
            return None
        return superArea

    @staticmethod
    def getAllSuperArea() -> list:
        if SuperArea._allSuperAreas:
            return SuperArea._allSuperAreas
        _allSuperAreas = GameData.getobjects(SuperArea.MODULE)
        return _allSuperAreas

    idAccessors: IdAccessors = IdAccessors(getSuperAreaById, getAllSuperArea)

    @property
    def name(self) -> str:
        if not self._name:
            self._name = I18n.getText(self.nameId)
        return self._name

    @property
    def worldmap(self) -> WorldMap:
        if not self._worldmap:
            if not self.hasWorldMap:
                self.worldmapId = 1
            self._worldmap = WorldMap.getWorldMapById(self.worldmapId)
        return self._worldmap
