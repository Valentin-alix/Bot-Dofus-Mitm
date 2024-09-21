import logging

from app.gui.signals import AppSignals
from app.interfaces.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.items.ObjectAddedMessage import (
    ObjectAddedMessage,
)
from app.interfaces.models.common import BotInfo, ParsedMessageHandler

logger = logging.getLogger(__name__)


class ObjectAddedMessageHandler(ParsedMessageHandler, ObjectAddedMessage):
    def handle(self, bot_info: BotInfo, app_signals: AppSignals) -> None:
        assert bot_info.common_info.character is not None
        logger.info(f"add object {self.object} to character")
        bot_info.common_info.character.on_object_added_msg(self.object)
