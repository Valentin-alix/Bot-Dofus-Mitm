import logging

from app.types_ import BotInfo
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeBidHouseItemAddOkMessage import (
    ExchangeBidHouseItemAddOkMessage,
)
from app.types_.parsed_message import ParsedMessageHandler

logger = logging.getLogger(__name__)


class ExchangeBidHouseItemAddOkMessageHandler(
    ParsedMessageHandler, ExchangeBidHouseItemAddOkMessage
):
    def handle(self, bot_info: BotInfo) -> None:
        with bot_info.selling_info.selling_hdv_with_lock.get("lock"):
            if (selling_hdv := bot_info.selling_info.selling_hdv_with_lock.get(
                    "selling_hdv")) is not None and selling_hdv.selected_object is not None:
                logger.info("Item was sold")
                if bot_info.selling_info.is_playing_event.is_set():
                    with bot_info.selling_info.on_sale_info_with_lock["lock"]:
                        bot_info.selling_info.on_sale_info_with_lock["number"] += 1
                        bot_info.selling_info.on_sale_info_with_lock["sum_price"] += self.itemInfo.objectPrice
                    selling_hdv.process()
