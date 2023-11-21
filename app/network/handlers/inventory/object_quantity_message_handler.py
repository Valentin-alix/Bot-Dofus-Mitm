import logging

from app.gui.signals import AppSignals
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.items.ObjectQuantityMessage import (
    ObjectQuantityMessage,
)
from app.types_.models.common import BotInfo, ParsedMessageHandler

logger = logging.getLogger(__name__)


class ObjectQuantityMessageHandler(ParsedMessageHandler, ObjectQuantityMessage):
    """When receiving new quantity of object"""

    def handle(self, bot_info: BotInfo, app_signals: AppSignals) -> None:
        assert bot_info.common_info.character is not None
        related_object_in_inventory = next(
            object_
            for object_ in bot_info.common_info.character.objects
            if object_.objectUID == self.objectUID
        )
        logger.info(f"change quantity of object {self.objectUID} to {self.quantity}")
        related_object_in_inventory.quantity = self.quantity
