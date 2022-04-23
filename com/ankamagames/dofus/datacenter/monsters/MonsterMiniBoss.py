from com.ankamagames.dofus.types.IdAccessors import IdAccessors
from com.ankamagames.jerakine.data.GameData import GameData


class MonsterMiniBoss:

    MODULE: str = "MonsterMiniBoss"

    @staticmethod
    def getMonsterById(id: int) -> "MonsterMiniBoss":
        return GameData.getObject(MonsterMiniBoss.MODULE, id)

    @staticmethod
    def getMonsters() -> list:
        return GameData.getObjects(MonsterMiniBoss.MODULE)

    idAccessors: IdAccessors = IdAccessors(getMonsterById, getMonsters)

    id: int

    monsterReplacingId: int
