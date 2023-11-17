from __future__ import annotations

import logging
from typing import Callable

from app.network.protocol import protocol, protocol_load
from app.types_.models.data import BufferInfos, Data

logger = logging.getLogger(__name__)


class Message:
    def __init__(self, message_id, data: Data, count: int | None = None):
        self.id = message_id
        if isinstance(data, bytearray):
            data = Data(data)
        self.data = data
        self.count = count

    @staticmethod
    def get_message_id(header: int) -> int:
        return header >> 2

    @staticmethod
    def get_message_length(src: Data, header: int) -> int:
        return int.from_bytes(src.read(header & 3), "big")

    @staticmethod
    def get_message_type_from_id(message_id: int) -> str:
        return protocol_load.msg_from_id[message_id]["name"]

    @staticmethod
    def get_json_from_message(message_type: str, message_data: Data) -> dict:
        return protocol.read(message_type, message_data)

    @staticmethod
    def get_message_from_json(_json: dict, count=None, random_hash=False) -> Message:
        type_name: str = _json["__type__"]
        type_id: int = protocol.types[type_name]["protocolId"]
        data = protocol.write(type_name, _json, random_hash=random_hash)
        return Message(type_id, data, count)

    @staticmethod
    def from_raw(
            from_client: bool,
            buffer_info: BufferInfos,
            on_error_callback: Callable | None = None,
    ) -> Message | None:
        if buffer_info.data.remaining() == 0:
            return None
        try:
            header = buffer_info.data.readUnsignedShort()
            if from_client:
                count = buffer_info.data.readUnsignedInt()
            else:
                count = None
            len_data = int.from_bytes(buffer_info.data.read(header & 3), "big")
            _id = header >> 2
            data = Data(buffer_info.data.read(len_data))
        except IndexError:
            buffer_info.data.pos = 0
            logger.info("Could not parse message: Not complete")
            return None
        if _id == 2:
            logger.info("Message is NetworkDataContainerMessage! Uncompressing...")
            new_buffer = BufferInfos(data=Data(data.readByteArray()))
            new_buffer.data.uncompress()
            msg = Message.from_raw(from_client, new_buffer)
            assert msg is not None and not new_buffer.data.remaining()
            return msg
        try:
            logger.debug("Parsed %s", protocol_load.msg_from_id[_id]["name"])
        except (KeyError, IndexError) as err:
            if on_error_callback is not None:
                on_error_callback(err)
            logger.error(f"Could not parse message, err: {str(err)}")
            buffer_info.reset()
            return None

        buffer_info.data.end()
        return Message(_id, data, count)

    @staticmethod
    def unpack_network_data_container_message(
            message_length, from_client, buffer_infos: BufferInfos
    ):
        logger.info("Received NetworkDataContainerMessage")
        if buffer_infos.data.remaining() >= message_length:
            buffer_network_data_container_message = BufferInfos(
                data=Data(buffer_infos.data.readByteArray())
            )
            buffer_network_data_container_message.data.uncompress()
            logger.info("Uncompressing NetworkDataContainerMessage")
            return Message.from_raw(from_client, buffer_network_data_container_message)
        return None

    @staticmethod
    def len_len_data(data: Data):
        if len(data) > 65535:
            return 3
        if len(data) > 255:
            return 2
        if len(data) > 0:
            return 1
        return 0

    def bytes(self):
        _header = 4 * self.id + self.len_len_data(self.data)
        data = Data()
        data.writeUnsignedShort(_header)
        if self.count is not None:
            data.writeUnsignedInt(self.count)
        data += len(self.data).to_bytes(self.len_len_data(self.data), "big")
        data += self.data
        return data.data
