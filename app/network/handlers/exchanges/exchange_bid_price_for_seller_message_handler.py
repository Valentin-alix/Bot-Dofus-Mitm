import logging

from app.gui.signals import AppSignals
from app.interfaces.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeBidPriceForSellerMessage import (
    ExchangeBidPriceForSellerMessage,
)
from app.interfaces.models.common import BotInfo, ParsedMessageHandler

logger = logging.getLogger(__name__)


class ExchangeBidPriceForSellerMessageHandler(
    ParsedMessageHandler, ExchangeBidPriceForSellerMessage
):
    """When receiving object for sells"""

    def handle(self, bot_info: BotInfo, app_signals: AppSignals) -> None:
        if (selling_hdv := bot_info.selling_info.selling_hdv) is not None:
            if (
                selling_hdv.selected_object is None
                or selling_hdv.selected_object["object_gid"] != self.genericId
            ):
                # when selected object is set to None before receiving
                return
            selling_hdv.selected_object["minimal_prices"] = self.minimalPrices
            logger.info(f"get minimal prices of selected object: {self.minimalPrices}")

            if bot_info.selling_info.is_playing_from_inventory_event.is_set():
                selling_hdv.process_from_inventory()

            if bot_info.selling_info.is_playing_update_event.is_set():
                selling_hdv.process_update()
