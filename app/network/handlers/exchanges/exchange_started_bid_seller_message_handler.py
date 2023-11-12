import logging

from app.modules.hdv.selling_hdv import SellingHdv
from app.types_ import BotInfo
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartedBidSellerMessage import (
    ExchangeStartedBidSellerMessage,
)
from app.types_.parsed_message import ParsedMessageHandler

logger = logging.getLogger(__name__)


class ExchangeStartedBidSellerMessageHandler(
    ParsedMessageHandler, ExchangeStartedBidSellerMessage
):
    """Received hdv info seller"""

    def handle(self, bot_info: BotInfo) -> None:
        with bot_info.selling_info.selling_hdv_with_lock.get("lock"):
            bot_info.selling_info.selling_hdv_with_lock["selling_hdv"] = SellingHdv(
                self.sellerDescriptor, bot_info
            )
            logger.info(f"got hdv seller with types : {self.sellerDescriptor.types}")
            if bot_info.selling_info.is_playing_event.is_set():
                bot_info.selling_info.selling_hdv_with_lock["selling_hdv"].process()
