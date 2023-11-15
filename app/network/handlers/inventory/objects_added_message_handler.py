import logging

from app.types_ import ParsedMessageHandler, BotInfo
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.items.ObjectsAddedMessage import \
    ObjectsAddedMessage

logger = logging.getLogger(__name__)


class ObjectsAddedMessageHandler(ParsedMessageHandler, ObjectsAddedMessage):
    def handle(self, bot_info: BotInfo) -> None:
        with bot_info.common_info.character_with_lock["lock"]:
            for _object in self.object:
                bot_info.common_info.character_with_lock["character"].on_object_added_msg(_object)
