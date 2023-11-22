import logging

from app.gui.signals import AppSignals
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeBidHouseSearchMessage import (
    ExchangeBidHouseSearchMessage,
)
from app.types_.models.common import ParsedMessageHandler, BotInfo

logger = logging.getLogger(__name__)


class ExchangeBidHouseSearchMessageHandler(
    ParsedMessageHandler, ExchangeBidHouseSearchMessage
):
    """from client, when placing object in hdv"""

    def handle(self, bot_info: BotInfo, app_signals: AppSignals) -> None:
        logger.info(f"received selected {self.follow} : {self.objectGID}")
        if (selling_hdv := bot_info.selling_info.selling_hdv) is not None:
            if self.follow is True:
                assert selling_hdv.selected_object is None
                selling_hdv.selected_object = {
                    "object_gid": self.objectGID,
                    "is_placed": False,
                }
            else:
                assert selling_hdv.selected_object is not None
                selling_hdv.selected_object = None

        elif (buying_hdv := bot_info.scraping_info.buying_hdv) is not None:
            if self.follow is True:
                assert buying_hdv.selected_object is None
                buying_hdv.selected_object = {
                    "object_gid": self.objectGID,
                    "is_placed": True,
                }
            else:
                assert buying_hdv.selected_object is not None
                buying_hdv.selected_object = None
