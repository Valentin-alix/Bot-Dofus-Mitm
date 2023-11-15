import logging

from app.types_ import DialogType, BotInfo
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeLeaveMessage import (
    ExchangeLeaveMessage,
)
from app.types_.parsed_message import ParsedMessageHandler

logger = logging.getLogger(__name__)


class ExchangeLeaveMessageHandler(ParsedMessageHandler, ExchangeLeaveMessage):
    """When leaving modal"""

    def handle(self, bot_info: BotInfo) -> None:
        if self.dialogType == DialogType.DIALOG_EXCHANGE:
            with bot_info.scraping_info.buying_hdv_with_lock.get("lock"):
                if (
                        buying_hdv := bot_info.scraping_info.buying_hdv_with_lock.get(
                            "buying_hdv"
                        )
                ) is not None:
                    logger.info("deleting buying hdv")
                    buying_hdv.stop_timer = True
                    bot_info.scraping_info.buying_hdv_with_lock["buying_hdv"] = None
            with bot_info.selling_info.selling_hdv_with_lock.get("lock"):
                if (
                        (selling_hdv := bot_info.selling_info.selling_hdv_with_lock.get("selling_hdv"))
                ) is not None:
                    logger.info("deleting selling hdv")
                    selling_hdv.stop_timer = True
                    bot_info.selling_info.selling_hdv_with_lock["selling_hdv"] = None
