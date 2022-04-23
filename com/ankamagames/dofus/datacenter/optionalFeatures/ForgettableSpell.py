from com.ankamagames.dofus.types.IdAccessors import IdAccessors
from com.ankamagames.jerakine.data.GameData import GameData
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter


class ForgettableSpell(IDataCenter):

    id: int

    pairId: int

    itemId: int

    MODULE: str = "ForgettableSpells"

    @classmethod
    def getForgettableSpells(cls) -> list["ForgettableSpell"]:
        return GameData.getObjects(cls.MODULE)

    @classmethod
    def getForgettableSpellById(cls, id: int) -> "ForgettableSpell":
        return GameData.getObject(cls.MODULE, id)

    idAccessors: IdAccessors = IdAccessors(
        getForgettableSpellById, getForgettableSpells
    )

    def __init__(self):
        super().__init__()

    def getForgettableSpellByScrollId(self, scrollId: int) -> "ForgettableSpell":
        forgettableSpell: ForgettableSpell = None
        forgettableSpells: list = self.getForgettableSpells()
        for forgettableSpell in forgettableSpells:
            if forgettableSpell.itemId == scrollId:
                return forgettableSpell
        return None
