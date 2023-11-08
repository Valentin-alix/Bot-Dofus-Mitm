import logging

import types_
from network.parsed_message.parsed_message_server.parsed_message_server import (
    ParsedMessageServer,
)

logger = logging.getLogger(__name__)


class ObjectQuantityMessage(ParsedMessageServer):
    """When receiving new quantity of object"""

    objectUID: int
    origin: int
    quantity: int

    def handle(self, threads_infos: types_.ThreadsInfos) -> None:
        with threads_infos.get("character_with_lock").get("lock"):
            if (
                character := threads_infos.get("character_with_lock").get("character")
            ) is not None:
                object_ = next(
                    (
                        object_
                        for object_ in character.objects
                        if object_.get("objectUID") == self.objectUID
                    ),
                    None,
                )
                if object_ is not None:
                    logger.info(
                        f"change quantity of object {self.objectUID} to {self.quantity}"
                    )
                    object_["quantity"] = self.quantity
