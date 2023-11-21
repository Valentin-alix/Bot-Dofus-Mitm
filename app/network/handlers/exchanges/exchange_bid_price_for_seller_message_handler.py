import logging

from app.gui.signals import AppSignals
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeBidPriceForSellerMessage import (
    ExchangeBidPriceForSellerMessage,
)
from app.types_.models.common import BotInfo, ParsedMessageHandler

logger = logging.getLogger(__name__)


class ExchangeBidPriceForSellerMessageHandler(
    ParsedMessageHandler, ExchangeBidPriceForSellerMessage
):
    """When selecting object for sells"""

    def handle(self, bot_info: BotInfo, app_signals: AppSignals) -> None:
        if (selling_hdv := bot_info.selling_info.selling_hdv) is not None:
            assert selling_hdv.selected_object is not None
            assert selling_hdv.selected_object["object_gid"] == self.genericId
            selling_hdv.selected_object["minimal_prices"] = self.minimalPrices
            logger.info(f"get minimal prices of selected object: {self.minimalPrices}")

            if bot_info.selling_info.is_playing_from_inventory_event.is_set():
                selling_hdv.process_from_inventory()

            if bot_info.selling_info.is_playing_update_event.is_set():
                selling_hdv.process_update()
