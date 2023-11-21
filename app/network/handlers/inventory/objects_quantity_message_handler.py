import logging

from app.gui.signals import AppSignals
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.items.ObjectsQuantityMessage import (
    ObjectsQuantityMessage,
)
from app.types_.models.common import BotInfo, ParsedMessageHandler

logger = logging.getLogger(__name__)


class ObjectsQuantityMessageHandler(ParsedMessageHandler, ObjectsQuantityMessage):
    """When receiving new quantity of object"""

    def handle(self, bot_info: BotInfo, app_signals: AppSignals) -> None:
        assert bot_info.common_info.character is not None
        for _object in self.objectsUIDAndQty:
            object_in_inventory = next(
                object_
                for object_ in bot_info.common_info.character.objects
                if object_.objectUID == _object.objectUID
            )
            logger.info(
                f"change quantity of object {_object.objectUID} to {_object.quantity}"
            )
            object_in_inventory.quantity = _object.quantity
