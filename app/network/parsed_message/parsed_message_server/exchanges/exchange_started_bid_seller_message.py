import logging

from modules.hdv.selling_hdv import SellingHdv
from network.parsed_message.dicts import ObjectItemToSellInBid, SellerBuyerDescriptor
from network.parsed_message.parsed_message_server.parsed_message_server import (
    ParsedMessageServer,
)
from types_ import ThreadsInfos

logger = logging.getLogger(__name__)


class ExchangeStartedBidSellerMessage(ParsedMessageServer):
    """Receiveid hdv infos seller"""

    objectsInfos: list[ObjectItemToSellInBid]
    sellerDescriptor: SellerBuyerDescriptor

    def handle(self, threads_infos: ThreadsInfos) -> None:
        with threads_infos.get("selling_hdv_with_lock").get("lock"):
            threads_infos["selling_hdv_with_lock"]["selling_hdv"] = SellingHdv(
                self.sellerDescriptor, threads_infos
            )
            logger.info(
                f"got hdv seller with types : {self.sellerDescriptor.get('types')}"
            )
            if threads_infos.get("event_play_hdv_selling").is_set():
                threads_infos["selling_hdv_with_lock"]["selling_hdv"].process()
