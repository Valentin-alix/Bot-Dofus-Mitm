import logging

import types_
from types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeTypesExchangerDescriptionForUserMessage import (
    ExchangeTypesExchangerDescriptionForUserMessage,
)
from types_.parsed_message import ParsedMessageHandler

logger = logging.getLogger(__name__)


class ExchangeTypesExchangerDescriptionForUserMessageHandler(
    ParsedMessageHandler, ExchangeTypesExchangerDescriptionForUserMessage
):
    """Received hdv object types after checking category"""

    def handle(self, threads_infos: types_.ThreadsInfos) -> None:
        with threads_infos.get("buying_hdv_with_lock").get("lock"):
            if (
                buying_hdv := threads_infos.get("buying_hdv_with_lock").get(
                    "buying_hdv"
                )
            ) is not None:
                buying_hdv.types_object = [
                    {"object_gid": type_description, "is_opened": False}
                    for type_description in self.typeDescription
                ]
                logger.info("Got type object of category")
                if threads_infos.get("event_play_hdv_scrapping").is_set():
                    buying_hdv.process()
