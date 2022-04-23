from com.ankamagames.dofus.types.IdAccessors import IdAccessors
from com.ankamagames.jerakine.data.GameData import GameData
from com.ankamagames.jerakine.data.I18n import I18n
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter


class SpellType(IDataCenter):

    MODULE: str = "SpellTypes"

    id: int

    longNameId: int

    shortNameId: int

    _longName: str

    _shortName: str

    def __init__(self):
        super().__init__()

    @classmethod
    def getSpellTypeById(cls, id: int) -> "SpellType":
        return GameData.getObject(cls.MODULE, id)

    idAccessors: IdAccessors = IdAccessors(getSpellTypeById, None)

    @property
    def longName(self) -> str:
        if not self._longName:
            self._longName = I18n.getText(self.longNameId)
        return self._longName

    @property
    def shortName(self) -> str:
        if not self._shortName:
            self._shortName = I18n.getText(self.shortNameId)
        return self._shortName
