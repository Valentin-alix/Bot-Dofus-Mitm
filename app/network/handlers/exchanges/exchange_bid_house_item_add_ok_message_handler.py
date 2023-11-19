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
    def handle(self, bot_info: BotInfo, app_signals: AppSignals) -> None:
        if (
                selling_hdv := bot_info.selling_info.selling_hdv
        ) is not None and selling_hdv.selected_object is not None:
            logger.info("Item was sold")
            if bot_info.selling_info.is_playing_event.is_set():
                bot_info.selling_info.on_sale_info_with_lock["number"] += 1
                bot_info.selling_info.on_sale_info_with_lock[
                    "sum_price"
                ] += self.itemInfo.objectPrice
                app_signals.on_new_sale_info.emit()
                selling_hdv.process()
