from __future__ import annotations
import logging

from network.parsed_message.parsed_message_server.parsed_message_server import (
    ParsedMessageServer,
)
import types_

logger = logging.getLogger(__name__)


class ObjectDeletedMessage(ParsedMessageServer):
    objectUID: int

    def handle(self, threads_infos: types_.ThreadsInfos) -> None:
        with threads_infos.get("character_with_lock").get("lock"):
            if (
                character := threads_infos.get("character_with_lock").get("character")
            ) is not None:
                logger.info(f"remove object {self.objectUID} to character")
                character.on_object_deleted_msg(self.objectUID)
