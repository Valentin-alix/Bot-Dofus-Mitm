import logging

import types_
from modules.character import Character
from types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.items.InventoryContentMessage import (
    InventoryContentMessage,
)
from types_.parsed_message import ParsedMessageHandler

logger = logging.getLogger(__name__)


class InventoryContentMessageHandler(ParsedMessageHandler, InventoryContentMessage):
    def handle(self, threads_infos: types_.ThreadsInfos) -> None:
        with threads_infos.get("character_with_lock").get("lock"):
            logger.info(f"Creating character with objects: {self.objects}")
            threads_infos["character_with_lock"]["character"] = Character(
                objects=self.objects
            )
