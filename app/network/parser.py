import logging
from typing import Optional
from queue import Queue
from network.models.message import Message
from network.models.data import Data

from network.handler import handle_message_unpacked
from network.protocol import protocol, protocol_load

logger = logging.getLogger(__name__)


class MessageRawDataParser:
    @staticmethod
    def get_message_type_from_id(message_id: int) -> str:
        return protocol_load.msg_from_id[message_id]["name"]

    @staticmethod
    def message_to_json(message_type: str, message_data: Data) -> dict:
        parsed_json = protocol.read(message_type, message_data)
        return parsed_json

    def parse(
        self,
        data: Data,
        message_id: int,
        message_length: int,
        from_client: bool,
        queue_handler_message: Queue[Message],
    ) -> Message | None:
        message_type = self.get_message_type_from_id(message_id)
        msg = Message(message_type=message_type, from_client=from_client)
        try:
            msg.content = MessageRawDataParser().message_to_json(
                message_type, Data(data.read(message_length))
            )
        except (KeyError, IndexError):
            logger.error(f"Could not parse {message_type}")
            return None

        queue_handler_message.put(msg)
        handle_message_unpacked(msg)
        return msg
