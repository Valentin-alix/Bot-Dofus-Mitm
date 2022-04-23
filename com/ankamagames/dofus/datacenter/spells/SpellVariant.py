from com.ankamagames.jerakine.data.GameData import GameData
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter
from com.ankamagames.jerakine.logger.Logger import Logger

logger = Logger(__name__)


class SpellVariant(IDataCenter):
    MODULE: str = "SpellVariants"

    id: int

    breedId: int

    spellIds: list[int]

    _spells: list

    def __init__(self):
        super().__init__()

    @classmethod
    def getSpellVariantById(cls, id: int) -> "SpellVariant":
        return GameData.getObject(cls.MODULE, id)

    @classmethod
    def getSpellVariants(cls) -> list["SpellVariant"]:
        return GameData.getObjects(cls.MODULE)

    @property
    def spells(self) -> list:
        from com.ankamagames.dofus.datacenter.spells.Spell import Spell

        if not self._spells:
            self._spells = list()
            for spellId in self.spellIds:
                spellToCopy = Spell.getSpellById(spellId)
                if spellToCopy:
                    self._spells.append(spellToCopy)
        return self._spells

    def __str__(self) -> str:
        result: str = ""
        result += "[Variante " + self.id + " : "
        name0: str = "???"
        name1: str = "???"
        id0: int = 0
        id1: int = 0
        if len(self.spells) and self.spells[0]:
            name0 = self.spells[0].name
        if len(self.spells) > 1 and self.spells[1]:
            name1 = self.spells[1].name
        if len(self.spellIds) and self.spellIds[0]:
            id0 = self.spellIds[0]
        if len(self.spellIds) > 1 and self.spellIds[1]:
            id1 = self.spellIds[1]
        return result + (name0 + " (" + id0 + ")" + ", " + name1 + " (" + id1 + ")]")
