import logging

from app.gui.signals import AppSignals
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeBidHouseItemAddOkMessage import (
    ExchangeBidHouseItemAddOkMessage,
)
from app.types_.models.common import BotInfo, ParsedMessageHandler

logger = logging.getLogger(__name__)


class ExchangeBidHouseItemAddOkMessageHandler(
    ParsedMessageHandler, ExchangeBidHouseItemAddOkMessage
):
    """Item was put on sale or updated"""

    def handle(self, bot_info: BotInfo, app_signals: AppSignals) -> None:
        logger.info("item was put on sale or updated")
        if (selling_hdv := bot_info.selling_info.selling_hdv) is not None:
            assert selling_hdv.selected_object is not None

            # updating object_on_sale_info
            selling_hdv.object_on_sale_info = [
                _object
                for _object in selling_hdv.object_on_sale_info
                if _object.objectUID != self.itemInfo.objectUID
            ]
            selling_hdv.object_on_sale_info.append(self.itemInfo)

            if bot_info.selling_info.is_playing_from_inventory_event.is_set():
                # processing from inventory
                bot_info.selling_info.on_sale_info_with_lock["number"] += 1
                bot_info.selling_info.on_sale_info_with_lock[
                    "sum_price"
                ] += self.itemInfo.objectPrice
                app_signals.on_new_sale_info.emit()

                selling_hdv.process_from_inventory()

            if bot_info.selling_info.is_playing_update_event.is_set():
                # processing update
                selling_hdv.close_selected_object()
