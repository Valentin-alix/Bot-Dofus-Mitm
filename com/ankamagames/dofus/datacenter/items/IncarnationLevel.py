from com.ankamagames.dofus.datacenter.items.Incarnation import Incarnation
from com.ankamagames.jerakine.data.GameData import GameData
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter


class IncarnationLevel(IDataCenter):

    MODULE: str = "IncarnationLevels"

    id: int

    incarnationId: int

    level: int

    requiredXp: int

    def __init__(self):
        super().__init__()

    @classmethod
    def getIncarnationLevelById(cls, id: int) -> "IncarnationLevel":
        return GameData.getObject(cls.MODULE, id)

    def getIncarnationLevelByIdAndLevel(
        self, incarnationId: int, level: int
    ) -> "IncarnationLevel":
        id: int = incarnationId * 100 + level
        return self.getIncarnationLevelById(id)

    @property
    def incarnation(self) -> Incarnation:
        return Incarnation.getIncarnationById(self.id)
