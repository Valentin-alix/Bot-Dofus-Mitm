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
        if (character := bot_info.common_info.character) is not None:
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
