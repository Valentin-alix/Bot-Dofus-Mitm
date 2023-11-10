import logging

from app.types_ import ThreadsInfos
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.items.ObjectAddedMessage import (
    ObjectAddedMessage,
)
from app.types_.parsed_message import ParsedMessageHandler

logger = logging.getLogger(__name__)


class ObjectAddedMessageHandler(ParsedMessageHandler, ObjectAddedMessage):
    def handle(self, threads_infos: ThreadsInfos) -> None:
        with threads_infos.get("character_with_lock").get("lock"):
            if (
                character := threads_infos.get("character_with_lock").get("character")
            ) is not None:
                logger.info(f"add object {self.object} to character")
                character.on_object_added_msg(self.object)
