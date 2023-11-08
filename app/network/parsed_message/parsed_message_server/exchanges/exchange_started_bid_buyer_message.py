import logging

import types_
from modules.hdv.buying_hdv import BuyingHdv
from network.parsed_message.dicts import SellerBuyerDescriptor
from network.parsed_message.parsed_message_server.parsed_message_server import (
    ParsedMessageServer,
)

logger = logging.getLogger(__name__)


class ExchangeStartedBidBuyerMessage(ParsedMessageServer):
    """Received hdv infos buyer"""

    buyerDescriptor: SellerBuyerDescriptor

    def handle(self, threads_infos: types_.ThreadsInfos) -> None:
        with threads_infos.get("buying_hdv_with_lock").get("lock"):
            threads_infos["buying_hdv_with_lock"]["buying_hdv"] = BuyingHdv(
                self.buyerDescriptor.get("types"), threads_infos
            )
            logger.info(
                f"got hdv buyer with types : {self.buyerDescriptor.get('types')}"
            )
            if threads_infos.get("event_play_hdv_scrapping").is_set():
                threads_infos["buying_hdv_with_lock"]["buying_hdv"].process()
