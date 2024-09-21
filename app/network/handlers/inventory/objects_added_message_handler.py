import logging

from app.gui.signals import AppSignals
from app.interfaces.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.items.ObjectsAddedMessage import (
    ObjectsAddedMessage,
)
from app.interfaces.models.common import BotInfo, ParsedMessageHandler

logger = logging.getLogger(__name__)


class ObjectsAddedMessageHandler(ParsedMessageHandler, ObjectsAddedMessage):
    def handle(self, bot_info: BotInfo, app_signals: AppSignals) -> None:
        assert bot_info.common_info.character is not None
        for _object in self.object:
            bot_info.common_info.character.on_object_added_msg(_object)
