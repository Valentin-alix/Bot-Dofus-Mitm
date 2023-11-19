import logging

from app.gui.signals import AppSignals
from app.modules.hdv.selling_hdv import SellingHdv
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartedBidSellerMessage import (
    ExchangeStartedBidSellerMessage,
)
from app.types_.models.common import BotInfo, ParsedMessageHandler

logger = logging.getLogger(__name__)


class ExchangeStartedBidSellerMessageHandler(
    ParsedMessageHandler, ExchangeStartedBidSellerMessage
):
    """Received hdv info seller"""

    def handle(self, bot_info: BotInfo, app_signals: AppSignals) -> None:
        bot_info.selling_info.selling_hdv = SellingHdv(
            self.sellerDescriptor, bot_info.selling_info.is_playing_event, bot_info.common_info.message_to_send_queue,
            bot_info.common_info.character
        )
        logger.info(f"got hdv seller with types : {self.sellerDescriptor.types}")
        if bot_info.selling_info.is_playing_event.is_set():
            bot_info.selling_info.selling_hdv.process()
