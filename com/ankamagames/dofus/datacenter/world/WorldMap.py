from com.ankamagames.dofus.types.IdAccessors import IdAccessors
import com.ankamagames.jerakine.data.GameData as gdata
from com.ankamagames.jerakine.data.I18n import I18n
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter


class WorldMap(IDataCenter):

    MODULE: str = "WorldMaps"

    id: int

    nameId: int

    origineX: int

    origineY: int

    mapWidth: float

    mapHeight: float

    viewableEverywhere: bool

    minScale: float

    maxScale: float

    startScale: float

    totalWidth: int

    totalHeight: int

    zoom: list[str]

    visibleOnMap: bool

    _name: str

    def __init__(self):
        super().__init__()

    @staticmethod
    def getWorldMapById(id: int) -> "WorldMap":
        return gdata.GameData.getObject(WorldMap.MODULE, id)

    @staticmethod
    def getAllWorldMaps() -> list:
        return gdata.GameData.getobjects(WorldMap.MODULE)

    idAccessors: IdAccessors = IdAccessors(getWorldMapById, getAllWorldMaps)

    @property
    def name(self) -> str:
        if not self._name:
            self._name = I18n.getText(self.nameId)
        return self._name
