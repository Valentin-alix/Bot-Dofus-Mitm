import logging

from modules.hdv.selling_hdv import SellingHdv
from types_ import ThreadsInfos
from types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartedBidSellerMessage import (
    ExchangeStartedBidSellerMessage,
)
from types_.parsed_message import ParsedMessageHandler

logger = logging.getLogger(__name__)


class ExchangeStartedBidSellerMessageHandler(
    ParsedMessageHandler, ExchangeStartedBidSellerMessage
):
    """Receiveid hdv infos seller"""

    def handle(self, threads_infos: ThreadsInfos) -> None:
        with threads_infos.get("selling_hdv_with_lock").get("lock"):
            threads_infos["selling_hdv_with_lock"]["selling_hdv"] = SellingHdv(
                self.sellerDescriptor, threads_infos
            )
            logger.info(f"got hdv seller with types : {self.sellerDescriptor.types}")
            if threads_infos.get("event_play_hdv_selling").is_set():
                threads_infos["selling_hdv_with_lock"]["selling_hdv"].process()
