import logging

from app.gui.signals import AppSignals
from app.modules.hdv.buying_hdv import BuyingHdv
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartedBidBuyerMessage import (
    ExchangeStartedBidBuyerMessage,
)
from app.types_.models.common import BotInfo, ParsedMessageHandler

logger = logging.getLogger(__name__)


class ExchangeStartedBidBuyerMessageHandler(
    ParsedMessageHandler, ExchangeStartedBidBuyerMessage
):
    """Received hdv info buyer"""

    def handle(self, bot_info: BotInfo, app_signals: AppSignals) -> None:
        # initialize scraping info buying hdv
        bot_info.scraping_info.buying_hdv = BuyingHdv(
            self.buyerDescriptor.types,
            bot_info.scraping_info.is_playing_event,
            app_signals,
            bot_info.common_info
        )
        logger.info(f"got hdv buyer with types : {self.buyerDescriptor.types}")
        if bot_info.scraping_info.is_playing_event.is_set():
            bot_info.scraping_info.buying_hdv.process()
