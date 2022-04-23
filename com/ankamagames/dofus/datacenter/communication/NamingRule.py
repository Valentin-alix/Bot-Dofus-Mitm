from com.ankamagames.dofus.types.IdAccessors import IdAccessors
from com.ankamagames.jerakine.data.GameData import GameData
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter
from com.ankamagames.jerakine.logger.Logger import Logger

logger = Logger(__name__)


class NamingRule(IDataCenter):

    MODULE: str = "NamingRules"

    id: int

    minLength: int

    maxLength: int

    regexp: str

    def __init__(self):
        super().__init__()

    @classmethod
    def getNamingRuleById(cls, id: int) -> "NamingRule":
        return GameData.getObject(cls.MODULE, id)

    @classmethod
    def getNamingRules(cls) -> list["NamingRule"]:
        return GameData.getObjects(cls.MODULE)

    idAccessors: IdAccessors = IdAccessors(getNamingRuleById, getNamingRules)
