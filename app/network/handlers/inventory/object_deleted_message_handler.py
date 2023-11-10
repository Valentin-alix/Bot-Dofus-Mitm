import logging

import types_
from types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.items.ObjectDeletedMessage import (
    ObjectDeletedMessage,
)
from types_.parsed_message import ParsedMessageHandler

logger = logging.getLogger(__name__)


class ObjectDeletedMessageHandler(ParsedMessageHandler, ObjectDeletedMessage):
    def handle(self, threads_infos: types_.ThreadsInfos) -> None:
        with threads_infos.get("character_with_lock").get("lock"):
            if (
                character := threads_infos.get("character_with_lock").get("character")
            ) is not None:
                logger.info(f"remove object {self.objectUID} to character")
                character.on_object_deleted_msg(self.objectUID)
