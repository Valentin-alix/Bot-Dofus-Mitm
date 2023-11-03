from __future__ import annotations

import logging
from typing import Callable, Dict
from pprint import pformat

from network.models.data import BufferInfos, Data
from network.protocol import protocol, protocol_load
from network.utils import BIT_RIGHT_SHIFT_LEN_PACKET_ID

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
        return header >> BIT_RIGHT_SHIFT_LEN_PACKET_ID

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
    def get_message_from_json(json, count=None, random_hash=False) -> Message:
        type_name: str = json["__type__"]
        type_id: int = protocol.types[type_name]["protocolId"]
        data = protocol.write(type_name, json, random_hash=random_hash)
        return Message(type_id, data, count)

    @staticmethod
    def from_raw(
        data: Data,
        from_client: bool,
        buffer_infos: BufferInfos,
        on_error_callback: Callable | None = None,
    ) -> Message | None:
        if not buffer_infos.splitted_packet:
            if data.remaining() < 2:
                return None
            header = data.readUnsignedShort()
            if from_client:
                count = data.readUnsignedInt()
            else:
                count = None
            try:
                message_length = Message.get_message_length(data, header)
                message_id = Message.get_message_id(header=header)
                message_type = Message.get_message_type_from_id(message_id)
            except (IndexError, KeyError) as err:
                logger.error(f"Could not get base info of message, error : {err}")
                if on_error_callback is not None:
                    on_error_callback(err)
                data.pos = 0
                return None

            if message_type == "NetworkDataContainerMessage":
                return Message.unpack_network_data_container_message(
                    data, message_length, from_client, buffer_infos
                )

            if data.remaining() >= message_length:
                msg = Message(
                    data=Data(data.read(message_length)),
                    count=count,
                    message_id=message_id,
                )
                return msg

            buffer_infos.data = Data(data.read(data.remaining()))

            buffer_infos.splitted_packet = {
                "id": message_id,
                "length": message_length,
                "count": count,
            }
            return None

        # Splitted packet
        if data.remaining() + len(
            buffer_infos.data
        ) >= buffer_infos.splitted_packet.get("length"):
            buffer_infos.data += data.read(
                buffer_infos.splitted_packet.get("length") - len(buffer_infos.data)
            )
            # Message is ready to be parsed
            msg = Message(
                data=Data(
                    buffer_infos.data.read(buffer_infos.splitted_packet.get("length"))
                ),
                message_id=buffer_infos.splitted_packet.get("id"),
                count=buffer_infos.splitted_packet.get("count"),
            )

            buffer_infos.splitted_packet = None
            buffer_infos.data = Data()
            return msg

        buffer_infos.data += data.read(data.remaining())
        return None

    @staticmethod
    def unpack_network_data_container_message(
        data: Data, message_length, from_client, buffer_infos
    ):
        logger.info("Received NetworkDataContainerMessage")
        if data.remaining() >= message_length:
            content_len = int(data.readVarInt())
            buffer_network_data_container_message = Data(data.read(content_len))
            buffer_network_data_container_message.uncompress()
            logger.info("Uncompressing NetworkDataContainerMessage")
            return Message.from_raw(
                buffer_network_data_container_message, from_client, buffer_infos
            )
        return None

    def len_len_data(self):
        if len(self.data) > 65535:
            return 3
        if len(self.data) > 255:
            return 2
        if len(self.data) > 0:
            return 1
        return 0

    def bytes(self):
        _header = 4 * self.id + self.len_len_data()
        data = Data()
        data.writeUnsignedShort(_header)
        if self.count is not None:
            data.writeUnsignedInt(self.count)
        data += len(self.data).to_bytes(self.len_len_data(), "big")
        data += self.data
        return data.data


class ParsedMessage:
    def __init__(self, from_client: bool, __type__: str, **kwargs) -> None:
        self.from_client = from_client
        self.__type__ = __type__
        for key, value in kwargs.items():
            self.__setattr__(key, value)

    def __str__(self) -> str:
        return pformat(vars(self))
