from com.ankamagames.dofus.types.IdAccessors import IdAccessors
from com.ankamagames.jerakine.data.GameData import GameData
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter
from com.ankamagames.jerakine.logger.Logger import Logger


class EvolutiveItemType(IDataCenter):

    MODULE: str = "EvolutiveItemTypes"

    logger = Logger(__name__)

    id: int

    maxLevel: int

    experienceBoost: float

    experienceByLevel: list[int]

    def __init__(self):
        super().__init__()

    @classmethod
    def getEvolutiveItemTypeById(cls, id: int) -> "EvolutiveItemType":
        return GameData.getObject(cls.MODULE, id)

    @classmethod
    def getEvolutiveItemTypes(cls) -> list:
        return GameData.getObjects(cls.MODULE)

    idAccessors = IdAccessors(getEvolutiveItemTypeById, getEvolutiveItemTypes)

    def getLevelFromExperiencePoints(self, experience: int) -> int:
        for i in range(self.maxLevel + 1):
            if self.experienceByLevel[i] > experience:
                break
            i += 1
        return i - 1

    def getMaxExperienceForLevel(self, level: int) -> int:
        experienceForNextLevel: int = self.experienceByLevel[level + 1]
        return experienceForNextLevel - 1
