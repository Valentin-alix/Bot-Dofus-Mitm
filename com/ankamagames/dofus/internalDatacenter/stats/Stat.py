from com.ankamagames.jerakine.logger.Logger import Logger
from damageCalculation.tools import StatIds

logger = Logger(__name__)


class Stat:

    UNKNOWN_STAT_NAME: str = "unknown"
    _entityId: float = None
    _id: float
    _totalValue: float = 0
    _name: str = None

    def __init__(self, id: float, totalValue: float):
        self._id = StatIds.UNKNOWN
        super()
        self._id = id
        self._totalValue = totalValue

    @property
    def entityId(self) -> float:
        return self._entityId

    @entityId.setter
    def entityId(self, entityId: float) -> None:
        self._entityId = entityId

    @property
    def id(self) -> float:
        return self._id

    @property
    def totalValue(self) -> float:
        return self._totalValue

    @totalValue.setter
    def totalValue(self, value: float) -> None:
        self._totalValue = value

    def __str__(self) -> str:
        return self.getFormattedMessage("total: " + self._totalValue.__str__())

    def reset(self) -> None:
        self._totalValue = 0

    def getFormattedMessage(self, message: str) -> str:
        return (
            self.__class__._name
            + " "
            + self._name
            + " (Entity ID: "
            + self._entityId.__str__()
            + ", ID: "
            + self._id.__str__()
            + "): "
            + message
        )
