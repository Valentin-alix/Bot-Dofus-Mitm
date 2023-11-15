import logging

from app.types_ import BotInfo
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.items.ObjectDeletedMessage import (
    ObjectDeletedMessage,
)
from app.types_.parsed_message import ParsedMessageHandler

logger = logging.getLogger(__name__)


class ObjectDeletedMessageHandler(ParsedMessageHandler, ObjectDeletedMessage):
    def handle(self, bot_info: BotInfo) -> None:
        with bot_info.common_info.character_with_lock.get("lock"):
            if (
                character := bot_info.common_info.character_with_lock.get("character")
            ) is not None:
                logger.info(f"remove object {self.objectUID} to character")
                character.on_object_deleted_msg(self.objectUID)
