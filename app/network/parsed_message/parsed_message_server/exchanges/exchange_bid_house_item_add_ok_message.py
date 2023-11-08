from __future__ import annotations
import logging

from network.parsed_message.dicts import ObjectItemToSellInBid
from network.parsed_message.parsed_message_server.parsed_message_server import (
    ParsedMessageServer,
)
import types_

logger = logging.getLogger(__name__)


class ExchangeBidHouseItemAddOkMessage(ParsedMessageServer):
    from_client: bool
    itemInfo: ObjectItemToSellInBid
    objectGID: int
    objectPrice: int
    objectUID: int
    quantity: int
    unsoldDelay: int

    def handle(self, threads_infos: types_.ThreadsInfos) -> None:
        if threads_infos.get("event_play_hdv_selling").is_set():
            with threads_infos.get("selling_hdv_with_lock").get("lock"):
                if (
                    selling_hdv := threads_infos.get("selling_hdv_with_lock").get(
                        "selling_hdv"
                    )
                ) is not None:
                    logger.info("Item was selled")
                    selling_hdv.process()
