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
        if (
                selling_hdv := bot_info.selling_info.selling_hdv
        ) is not None:
            logger.info("get selected object")

            _object_in_inventory = next(
                (
                    _object
                    for _object in bot_info.common_info.character.objects
                    if _object.objectGID == self.genericId
                ),
                None,
            )
            if _object_in_inventory is not None:
                selling_hdv.selected_object = {
                    "quantity": _object_in_inventory.quantity,
                    "all_identical": self.allIdentical,
                    "object_gid": self.genericId,
                    "object_uid": _object_in_inventory.objectUID,
                    "is_placed": True,
                    "minimal_prices": self.minimalPrices,
                }
                logger.info(selling_hdv.selected_object)
            else:
                logger.info(f"object not found in inventory, cleaning : {selling_hdv.selected_object['object_gid']}")
                selling_hdv.clean_selected_object()

            if bot_info.selling_info.is_playing_event.is_set():
                selling_hdv.process()
        else:
            raise ValueError("SellerHdv should not be None")
