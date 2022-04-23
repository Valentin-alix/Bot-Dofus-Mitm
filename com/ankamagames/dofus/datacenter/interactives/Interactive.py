from com.ankamagames.dofus.types.IdAccessors import IdAccessors
from com.ankamagames.jerakine.data.GameData import GameData
from com.ankamagames.jerakine.data.I18n import I18n
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter


class Interactive(IDataCenter):

    MODULE: str = "Interactives"

    id: int

    nameId: int

    actionId: int

    displayTooltip: bool

    _name: str

    def __init__(self):
        super().__init__()

    @classmethod
    def getInteractiveById(cls, id: int) -> "Interactive":
        return GameData.getObject(cls.MODULE, id)

    @classmethod
    def getInteractives(cls) -> list["Interactive"]:
        return GameData.getObjects(cls.MODULE)

    idAccessors: IdAccessors = IdAccessors(getInteractiveById, getInteractives)

    @property
    def name(self) -> str:
        if not self._name:
            self._name = I18n.getText(self.nameId)
        return self._name
