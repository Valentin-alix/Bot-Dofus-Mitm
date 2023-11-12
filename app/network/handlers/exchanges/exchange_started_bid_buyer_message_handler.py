import logging

from app.modules.hdv.buying_hdv import BuyingHdv
from app.types_ import BotInfo
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartedBidBuyerMessage import (
    ExchangeStartedBidBuyerMessage,
)
from app.types_.parsed_message import ParsedMessageHandler

logger = logging.getLogger(__name__)


class ExchangeStartedBidBuyerMessageHandler(
    ParsedMessageHandler, ExchangeStartedBidBuyerMessage
):
    """Received hdv info buyer"""

    def handle(self, bot_info: BotInfo) -> None:
        with bot_info.scraping_info.buying_hdv_with_lock.get("lock"):
            bot_info.scraping_info.buying_hdv_with_lock["buying_hdv"] = BuyingHdv(
                self.buyerDescriptor.types, bot_info
            )
            logger.info(f"got hdv buyer with types : {self.buyerDescriptor.types}")
            if bot_info.scraping_info.is_playing_event.is_set():
                bot_info.scraping_info.buying_hdv_with_lock["buying_hdv"].process()
