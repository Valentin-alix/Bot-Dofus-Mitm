import logging

from database import execute_sql
from models.data import Data
from network.messages.exchange_craft_result_magic_with_object_desc_message import (
    ExchangeCraftResultMagicWithObjectDescMessage,
)
from network.messages.exchange_object_added_message import ExchangeObjectAddedMessage

logger = logging.getLogger(__name__)


class MessageRawDataParser:
    message_class_by_name = {
        "ExchangeCraftResultMagicWithObjectDescMessage": ExchangeCraftResultMagicWithObjectDescMessage,
        "ExchangeObjectAddedMessage": ExchangeObjectAddedMessage,
    }

    def parse(self, input, messageId, messageLength):
        messageType = execute_sql(
            "select name from message_network where protocol_id = ?", (messageId,)
        )
        if len(messageType) == 0:
            logger.error(
                "Unknown packet received (ID "
                + str(messageId)
                + ", length "
                + str(messageLength)
                + ")"
            )
            return None
        logger.info(f"Message: {messageType}")

        message_data = Data(input.read(messageLength))

        if (
            class_name := self.message_class_by_name.get(messageType[0][0], None)
        ) is not None:
            class_name().deserialize(message_data)

        return message_data
