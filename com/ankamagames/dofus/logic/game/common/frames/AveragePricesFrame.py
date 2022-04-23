from datetime import datetime
from com.ankamagames.dofus.kernel.net.ConnectionsHandler import ConnectionsHandler
from com.ankamagames.dofus.logic.common.managers.PlayerManager import PlayerManager
from com.ankamagames.dofus.logic.game.common.managers.FeatureManager import (
    FeatureManager,
)
from com.ankamagames.dofus.network.enums.GameContextEnum import GameContextEnum
from com.ankamagames.dofus.network.messages.game.context.GameContextCreateMessage import (
    GameContextCreateMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.ObjectAveragePricesErrorMessage import (
    ObjectAveragePricesErrorMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.ObjectAveragePricesGetMessage import (
    ObjectAveragePricesGetMessage,
)
from com.ankamagames.dofus.network.messages.game.inventory.ObjectAveragePricesMessage import (
    ObjectAveragePricesMessage,
)
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.managers.StoreDataManager import StoreDataManager
from com.ankamagames.jerakine.messages.Frame import Frame
from com.ankamagames.jerakine.messages.Message import Message
from com.ankamagames.jerakine.types.DataStoreType import DataStoreType
from com.ankamagames.jerakine.types.enums.DataStoreEnum import DataStoreEnum
from com.ankamagames.jerakine.types.enums.Priority import Priority

logger = Logger(__name__)


class AveragePricesFrame(Frame):

    _dataStoreType: DataStoreType

    _serverName: str

    _pricesData: object

    def __init__(self):
        super().__init__()
        self._serverName = PlayerManager().server.name
        if not self._dataStoreType:
            self._dataStoreType = DataStoreType(
                "itemAveragePrices",
                True,
                DataStoreEnum.LOCATION_LOCAL,
                DataStoreEnum.BIND_COMPUTER,
            )

    @property
    def priority(self) -> int:
        return Priority.NORMAL

    @property
    def dataAvailable(self) -> bool:
        return self._pricesData

    @property
    def pricesData(self) -> object:
        return self._pricesData

    def pushed(self) -> bool:
        self._pricesData = StoreDataManager().getData(
            self._dataStoreType, self._serverName
        )
        return True

    def pulled(self) -> bool:
        return True

    def process(self, pMsg: Message) -> bool:
        if isinstance(pMsg, GameContextCreateMessage):
            gccm = pMsg
            if gccm.context == GameContextEnum.ROLE_PLAY and self.updateAllowed():
                self.askPricesData()
            return False
        if isinstance(pMsg, ObjectAveragePricesMessage):
            oapm = pMsg
            self.updatePricesData(oapm.ids, oapm.avgPrices)
            return True
        if isinstance(pMsg, ObjectAveragePricesErrorMessage):
            return True
        else:
            return False

    def updatePricesData(
        self, pItemsIds: list[int], pItemsAvgPrices: list[float]
    ) -> None:
        nbItems: int = len(pItemsIds)
        self._pricesData = {"lastUpdate": datetime.now(), "items": dict()}
        for i in range(nbItems):
            self._pricesData.items[pItemsIds[i]] = pItemsAvgPrices[i]
        StoreDataManager().setData(
            self._dataStoreType, self._serverName, self._pricesData
        )

    def updateAllowed(self) -> bool:
        featureManager: FeatureManager = FeatureManager()
        if not featureManager or not featureManager.isFeatureWithKeywordEnabled(
            "trade.averagePricesAutoUpdate"
        ):
            return False
        if self.dataAvailable:
            now = datetime.now()
            lastUpdateHour = self._pricesData.lastUpdate.hour
            if (
                now.getFullYear() == self._pricesData.lastUpdate.getFullYear()
                and now.getMonth() == self._pricesData.lastUpdate.getMonth()
                and now.getDate() == self._pricesData.lastUpdate.getDate()
            ):
                return False
        return True

    def askPricesData(self) -> None:
        oapgm: ObjectAveragePricesGetMessage = ObjectAveragePricesGetMessage()
        oapgm.init()
        ConnectionsHandler.getConnection().send(oapgm)
