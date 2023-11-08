import logging

import types_
from network.parsed_message.dicts import ObjectItem
from network.parsed_message.parsed_message_server.parsed_message_server import (
    ParsedMessageServer,
)

logger = logging.getLogger(__name__)


class ObjectAddedMessage(ParsedMessageServer):
    object: ObjectItem
    origin: int

    def handle(self, threads_infos: types_.ThreadsInfos) -> None:
        with threads_infos.get("character_with_lock").get("lock"):
            if (
                character := threads_infos.get("character_with_lock").get("character")
            ) is not None:
                logger.info(f"add object {self.object} to character")
                character.on_object_added_msg(self.object)
