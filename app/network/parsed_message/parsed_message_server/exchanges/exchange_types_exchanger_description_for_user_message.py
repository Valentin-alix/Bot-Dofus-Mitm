import logging

import types_
from network.parsed_message.parsed_message_server.parsed_message_server import (
    ParsedMessageServer,
)

logger = logging.getLogger(__name__)


class ExchangeTypesExchangerDescriptionForUserMessage(ParsedMessageServer):
    """Received hdv object types after checking category"""

    objectType: int
    typeDescription: list[int]

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
