from __future__ import annotations
import logging

from modules.character import Character
from network.parsed_message.dicts import ObjectItem
from network.parsed_message.parsed_message_server.parsed_message_server import (
    ParsedMessageServer,
)
import types_

logger = logging.getLogger(__name__)


class InventoryContentMessage(ParsedMessageServer):
    kamas: int
    objects: list[ObjectItem]

    def handle(self, threads_infos: types_.ThreadsInfos) -> None:
        with threads_infos.get("character_with_lock").get("lock"):
            logger.info(f"Creating character with objects: {self.objects}")
            threads_infos["character_with_lock"]["character"] = Character(
                objects=self.objects
            )
