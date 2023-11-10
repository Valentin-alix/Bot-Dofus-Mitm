import logging

from app.types_ import ThreadsInfos
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeBidPriceForSellerMessage import (
    ExchangeBidPriceForSellerMessage,
)
from app.types_.parsed_message import ParsedMessageHandler

logger = logging.getLogger(__name__)


class ExchangeBidPriceForSellerMessageHandler(
    ParsedMessageHandler, ExchangeBidPriceForSellerMessage
):
    """When selecting object for sells"""

    def handle(self, threads_infos: ThreadsInfos) -> None:
        with threads_infos.get("selling_hdv_with_lock").get("lock"):
            if (
                selling_hdv := threads_infos.get("selling_hdv_with_lock").get(
                    "selling_hdv"
                )
            ) is not None:
                logger.info("get selected object")
                name_selected_object = selling_hdv.get_name_by_generic_id(
                    self.genericId
                )
                selling_hdv.selected_object = {
                    "all_identical": self.allIdentical,
                    "generic_id": self.genericId,
                    "is_placed": True,
                    "minimal_prices": self.minimalPrices,
                    "name": name_selected_object,
                }
                if threads_infos.get("event_play_hdv_selling").is_set():
                    selling_hdv.process()
