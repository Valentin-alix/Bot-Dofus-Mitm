import logging

import types_
from types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.items.ObjectsQuantityMessage import (
    ObjectsQuantityMessage,
)
from types_.parsed_message import ParsedMessageHandler

logger = logging.getLogger(__name__)


class ObjectsQuantityMessageHandler(ParsedMessageHandler, ObjectsQuantityMessage):
    """When receiving new quantity of object"""

    def handle(self, threads_infos: types_.ThreadsInfos) -> None:
        with threads_infos.get("character_with_lock").get("lock"):
            if (
                character := threads_infos.get("character_with_lock").get("character")
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
                    object_["quantity"] = self.quantity
