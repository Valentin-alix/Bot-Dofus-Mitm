import logging

from app.types_ import ThreadsInfos
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeBidHouseItemAddOkMessage import (
    ExchangeBidHouseItemAddOkMessage,
)
from app.types_.parsed_message import ParsedMessageHandler

logger = logging.getLogger(__name__)


class ExchangeBidHouseItemAddOkMessageHandler(
    ParsedMessageHandler, ExchangeBidHouseItemAddOkMessage
):
    def handle(self, threads_infos: ThreadsInfos) -> None:
        if threads_infos.get("event_play_hdv_selling").is_set():
            with threads_infos.get("selling_hdv_with_lock").get("lock"):
                if (
                    selling_hdv := threads_infos.get("selling_hdv_with_lock").get(
                        "selling_hdv"
                    )
                ) is not None:
                    if selling_hdv.selected_object is not None:
                        threads_infos["queue_for_sale_object"].put(
                            selling_hdv.selected_object
                        )
                    logger.info("Item was selled")
                    selling_hdv.process()
