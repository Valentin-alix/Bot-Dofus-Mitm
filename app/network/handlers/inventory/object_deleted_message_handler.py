import logging

from app.gui.signals import AppSignals
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.items.ObjectDeletedMessage import (
    ObjectDeletedMessage,
)
from app.types_.models.common import BotInfo, ParsedMessageHandler

logger = logging.getLogger(__name__)


class ObjectDeletedMessageHandler(ParsedMessageHandler, ObjectDeletedMessage):
    def handle(self, bot_info: BotInfo, app_signals: AppSignals) -> None:
        assert bot_info.common_info.character is not None
        logger.info(f"remove object {self.objectUID} to character")
        bot_info.common_info.character.on_object_deleted_msg(self.objectUID)
