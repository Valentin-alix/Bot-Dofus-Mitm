import logging

from app.gui.signals import AppSignals
from app.interfaces.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeLeaveMessage import (
    ExchangeLeaveMessage,
)
from app.interfaces.enums import DialogType
from app.interfaces.models.common import BotInfo, ParsedMessageHandler

logger = logging.getLogger(__name__)


class ExchangeLeaveMessageHandler(ParsedMessageHandler, ExchangeLeaveMessage):
    """When leaving modal"""

    def handle(self, bot_info: BotInfo, app_signals: AppSignals) -> None:
        if self.dialogType == DialogType.DIALOG_EXCHANGE:
            app_signals.on_leaving_hdv.emit()
            # clearing buying hdv or selling hdv
            if (buying_hdv := bot_info.scraping_info.buying_hdv) is not None:
                logger.info("deleting buying hdv")
                buying_hdv.stop_timer = True
                bot_info.scraping_info.buying_hdv = None

            if (selling_hdv := bot_info.selling_info.selling_hdv) is not None:
                logger.info("deleting selling hdv")
                selling_hdv.stop_timer = True
                bot_info.selling_info.selling_hdv = None
