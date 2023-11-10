import logging

from app.modules.hdv.buying_hdv import BuyingHdv
from app.types_ import ThreadsInfos
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartedBidBuyerMessage import (
    ExchangeStartedBidBuyerMessage,
)
from app.types_.parsed_message import ParsedMessageHandler

logger = logging.getLogger(__name__)


class ExchangeStartedBidBuyerMessageHandler(
    ParsedMessageHandler, ExchangeStartedBidBuyerMessage
):
    """Received hdv infos buyer"""

    def handle(self, threads_infos: ThreadsInfos) -> None:
        with threads_infos.get("buying_hdv_with_lock").get("lock"):
            threads_infos["buying_hdv_with_lock"]["buying_hdv"] = BuyingHdv(
                self.buyerDescriptor.types, threads_infos
            )
            logger.info(f"got hdv buyer with types : {self.buyerDescriptor.types}")
            if threads_infos.get("event_play_hdv_scrapping").is_set():
                threads_infos["buying_hdv_with_lock"]["buying_hdv"].process()
