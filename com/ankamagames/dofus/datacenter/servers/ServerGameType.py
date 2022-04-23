from com.ankamagames.dofus.types.IdAccessors import IdAccessors
from com.ankamagames.jerakine.data.GameData import GameData
from com.ankamagames.jerakine.data.I18n import I18n
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter
from com.ankamagames.jerakine.logger.Logger import Logger

logger = Logger(__name__)


class ServerGameType(IDataCenter):

    MODULE: str = "ServerGameTypes"

    id: int

    selectableByPlayer: bool

    nameId: int

    rulesId: int

    descriptionId: int

    _name: str

    _rules: str

    _description: str

    def __init__(self):
        super().__init__()

    @classmethod
    def getServerGameTypeById(cls, id: int) -> "ServerGameType":
        return GameData.getObject(cls.MODULE, id)

    @classmethod
    def getServerGameTypes(cls) -> list["ServerGameType"]:
        return GameData.getObjects(cls.MODULE)

    idAccessors: IdAccessors = IdAccessors(getServerGameTypeById, getServerGameTypes)

    @property
    def name(self) -> str:
        if not self._name:
            self._name = I18n.getText(self.nameId)
        return self._name

    @property
    def rules(self) -> str:
        if not self._rules:
            self._rules = I18n.getText(self.rulesId)
        return self._rules

    @property
    def description(self) -> str:
        if not self._description:
            self._description = I18n.getText(self.descriptionId)
        return self._description
