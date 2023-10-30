import logging
from models.message import Message

from models.data import Data
from network.handler import handle_message_unpacked
from network.protocol import protocol, protocol_load

logger = logging.getLogger(__name__)


class MessageRawDataParser:
    @staticmethod
    def get_message_type_from_id(message_id):
        return protocol_load.msg_from_id[message_id]["name"]

    @staticmethod
    def message_to_json(message_type, message_data):
        parsed_json = protocol.read(message_type, message_data)
        return parsed_json

    def parse(self, data: Data, message_id, message_length) -> Message:
        message_type = self.get_message_type_from_id(message_id)

        msg = Message(message_type=message_type)
        msg.content = MessageRawDataParser().message_to_json(
            message_type, Data(data.read(message_length))
        )

        handle_message_unpacked(msg)
        return msg
