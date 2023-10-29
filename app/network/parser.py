import logging

from database import execute_sql
from models.data import Data
from models.utils import UnpackMode
from network.handler import handle_message_content
from network.protocol import protocol

logger = logging.getLogger(__name__)


class MessageRawDataParser:
    unpack_modes = {4506: UnpackMode.ASYNC}

    @staticmethod
    def message_to_json(message_type, message_data):
        logger.debug("Getting json representation of message")
        parsed_json = protocol.read(message_type, message_data)
        return parsed_json

    def parse(self, data: Data, message_id, message_length):
        try:
            message_type = execute_sql(
                "select name from message_network where protocol_id = ?", (message_id,)
            )[0][0]
        except IndexError:
            logger.error(
                "Unknown packet received (ID "
                + str(message_id)
                + ", length "
                + str(message_length)
                + ")"
            )
            return None
        logger.info(f"Message: {message_type} with id : {message_id}")
        message_data = Data(data.read(message_length))
        msg = {
            "unpacked": True,
            "type_message": message_type,
        }
        if message_type == "NetworkDataContainerMessage":
            msg["content"] = message_data
            return msg
        try:
            message_content = MessageRawDataParser().message_to_json(
                message_type, message_data
            )
            logger.info(f"{message_type} parsed : {message_content}")
        except Exception as err:
            logger.error(
                f"Parsing error for message {message_type} with id : {message_id} | error : {err}"
            )
            return None
        msg["content_json"] = message_content

        handle_message_content(msg["content_json"], message_type)

        return msg

    def parse_async(self, data: Data, message_id, message_length):
        try:
            message_type = execute_sql(
                "select name from message_network where protocol_id = ?", (message_id,)
            )[0][0]
        except IndexError:
            logger.error(
                "Unknown packet received (ID "
                + str(message_id)
                + ", length "
                + str(message_length)
                + ")"
            )
            return None
        logger.info(f"Message async: {message_type} with id : {message_id}")
        message_data = Data(data.read(message_length))
        msg = {"unpacked": False, "type_message": message_type}
        if message_type == "NetworkDataContainerMessage":
            msg["content"] = message_data
            return msg
        try:
            message_content = MessageRawDataParser().message_to_json(
                message_type, message_data
            )
        except Exception as err:
            logger.error(
                f"Parsing error for message {message_type} with id : {message_id} | error : {err}"
            )
            return None
        msg["content_json"] = message_content

        handle_message_content(msg["content_json"], message_type)

        return msg

    def get_unpack_mode(self, message_id):
        return (
            int(self.unpack_modes[message_id])
            if message_id in self.unpack_modes
            else UnpackMode.DEFAULT
        )
