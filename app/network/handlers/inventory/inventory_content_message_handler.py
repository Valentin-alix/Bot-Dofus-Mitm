import logging

from app.gui.signals import AppSignals
from app.interfaces.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.items.InventoryContentMessage import (
    InventoryContentMessage,
)
from app.interfaces.models.common import BotInfo, ParsedMessageHandler
from app.modules.character import Character

logger = logging.getLogger(__name__)


class InventoryContentMessageHandler(ParsedMessageHandler, InventoryContentMessage):
    def handle(self, bot_info: BotInfo, app_signals: AppSignals) -> None:
        logger.info(f"Creating character with objects: {self.objects}")
        bot_info.common_info.character = Character(objects=self.objects)
