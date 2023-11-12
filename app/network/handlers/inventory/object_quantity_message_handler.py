import logging

from app.types_ import BotInfo
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.items.ObjectQuantityMessage import \
    ObjectQuantityMessage
from app.types_.parsed_message import ParsedMessageHandler

logger = logging.getLogger(__name__)


class ObjectQuantityMessageHandler(ParsedMessageHandler, ObjectQuantityMessage):
    """When receiving new quantity of object"""

    def handle(self, bot_info: BotInfo) -> None:
        with bot_info.common_info.character_with_lock.get("lock"):
            if (
                    character := bot_info.common_info.character_with_lock.get("character")
            ) is not None:
                object_ = next(
                    (
                        object_
                        for object_ in character.objects
                        if object_.objectUID == self.objectUID
                    ),
                    None,
                )
                if object_ is not None:
                    logger.info(
                        f"change quantity of object {self.objectUID} to {self.quantity}"
                    )
                    object_.quantity = self.quantity
