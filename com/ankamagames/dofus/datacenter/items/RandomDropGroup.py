from com.ankamagames.dofus.datacenter.items.RandomDropItem import RandomDropItem
from com.ankamagames.jerakine.data.GameData import GameData
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter


class RandomDropGroup(IDataCenter):

    MODULE: str = "RandomDropGroups"

    id: int

    name: str

    description: str

    randomDropItems: list[RandomDropItem]

    displayContent: bool

    displayChances: bool

    _groupWeight: int

    def __init__(self):
        super().__init__()

    @classmethod
    def getRandomDropGroupById(cls, id: int) -> "RandomDropGroup":
        return GameData.getObject(cls.MODULE, id)

    @classmethod
    def getAllRandomDropGroup(cls) -> list:
        return GameData.getObjects(cls.MODULE)

    @property
    def groupWeight(self) -> int:
        item: RandomDropItem = None
        self._groupWeight = 0
        for item in self.randomDropItems:
            self._groupWeight += item.probability
        return self._groupWeight
