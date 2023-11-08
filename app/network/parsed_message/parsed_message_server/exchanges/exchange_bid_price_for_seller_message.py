import logging

import types_
from network.parsed_message.parsed_message_server.parsed_message_server import (
    ParsedMessageServer,
)

logger = logging.getLogger(__name__)


class ExchangeBidPriceForSellerMessage(ParsedMessageServer):
    """When selecting object for sells"""

    allIdentical: bool
    averagePrice: int
    from_client: bool
    genericId: int
    minimalPrices: list[int]

    def handle(self, threads_infos: types_.ThreadsInfos) -> None:
        with threads_infos.get("selling_hdv_with_lock").get("lock"):
            if (
                selling_hdv := threads_infos.get("selling_hdv_with_lock").get(
                    "selling_hdv"
                )
            ) is not None:
                logger.info("get selected object")
                selling_hdv.selected_object = {
                    "all_identical": self.allIdentical,
                    "generic_id": self.genericId,
                    "is_placed": True,
                    "minimal_prices": self.minimalPrices,
                }
                if threads_infos.get("event_play_hdv_selling").is_set():
                    selling_hdv.process()
