import logging
from typing import Optional
from network.utils import FILTER_DOFUS, get_local_ip

from network.models.data import Buffer, Data
from network.models.message import Message
from network.utils import NetworkMessage
from network.parser import MessageRawDataParser
from scapy.all import Packet, Raw, sniff
from scapy.layers.inet import IP, TCP

logger = logging.getLogger(__name__)


class Sniffer:
    def __init__(self, capture_path: Optional[str] = None):
        self.not_completed_message_number: int = 0
        self.capture_path: str | None = capture_path
        self.raw_parser: MessageRawDataParser = MessageRawDataParser()
        self.async_network_data_container_message = Data()
        self.buffer_infos_from_server = Buffer()
        self.buffer_infos_from_client = Buffer()
        self.ip_local = get_local_ip()

    def launch_sniffer(self) -> None:
        if self.capture_path:
            sniff(prn=self.on_receive, offline=self.capture_path)
        else:
            sniff(prn=self.on_receive, store=False, filter=FILTER_DOFUS)

    def on_receive(self, packet: Packet):
        if Raw in packet:
            src_ip: int = packet[IP].src
            data = Data(packet[Raw].load)
            logger.info(f"Received Packet : Raw : {str(data)} \n src IP : {src_ip}")
            self.receive(data, src_ip == self.ip_local)

    def receive(self, data: Data, from_client: bool):
        if data.remaining() > 0:
            msg = self.low_receive(data, from_client)
            while msg is not None:
                msg = self.low_receive(data, from_client)

    def low_receive(self, src: Data, from_client: bool) -> Message | None:
        _buffer_infos = (
            self.buffer_infos_from_client
            if from_client
            else self.buffer_infos_from_server
        )

        if not _buffer_infos.is_splitted_packet:
            if src.remaining() < 2:
                return None

            header = src.readUnsignedShort()

            if from_client:
                src.readUnsignedInt()

            try:
                message_length = int.from_bytes(src.read(header & 3), "big")
                message_id = header >> NetworkMessage.BIT_RIGHT_SHIFT_LEN_PACKET_ID
            except IndexError:
                logger.error("Could not get message length or id")
                self.not_completed_message_number += 1
                src.pos = 0
                return None

            try:
                message_type = MessageRawDataParser().get_message_type_from_id(
                    message_id
                )
            except (IndexError, KeyError):
                logger.error(f"Could not get type for id : {message_id}")
                self.not_completed_message_number += 1
                src.pos = 0
                return None

            if message_type == "NetworkDataContainerMessage":
                logger.info("Received NetworkDataContainerMessage")
                if src.remaining() >= message_length:
                    content_len = int(src.readVarInt())
                    buffer_network_data_container_message = Data(src.read(content_len))
                    buffer_network_data_container_message.uncompress()
                    self.async_network_data_container_message = Data()
                    logger.info("Uncompressing NetworkDataContainerMessage")
                    return self.low_receive(
                        buffer_network_data_container_message, from_client
                    )
                self.async_network_data_container_message += src
                return None

            if src.remaining() >= (header & NetworkMessage.BIT_MASK):
                if src.remaining() >= message_length:
                    msg = self.raw_parser.parse(src, message_id, message_length)
                    return msg

                _buffer_infos.static_header = None
                _buffer_infos.buffer_data = Data(src.read(src.remaining()))
            else:
                _buffer_infos.static_header = header

            _buffer_infos.splitted_packet_length = message_length
            _buffer_infos.splitted_packet_id = message_id
            _buffer_infos.is_splitted_packet = True
            return None

        # is splitted packets
        if _buffer_infos.static_header is not None:
            _buffer_infos.splitted_packet_length = int.from_bytes(
                src.read(_buffer_infos.static_header & 3), "big"
            )
            _buffer_infos.static_header = None

        if (
            _buffer_infos.splitted_packet_length is not None
            and _buffer_infos.splitted_packet_id is not None
        ):
            if (
                src.remaining() + len(_buffer_infos.buffer_data)
                >= _buffer_infos.splitted_packet_length
            ):
                _buffer_infos.buffer_data += src.read(
                    _buffer_infos.splitted_packet_length
                    - len(_buffer_infos.buffer_data)
                )
                _buffer_infos.buffer_data.pos = 0

                msg = self.raw_parser.parse(
                    _buffer_infos.buffer_data,
                    _buffer_infos.splitted_packet_id,
                    _buffer_infos.splitted_packet_length,
                )

                _buffer_infos.is_splitted_packet = False
                _buffer_infos.buffer_data = Data()
                return msg
        else:
            raise ValueError(
                "splitted_packet_length and splitted_packet_id should not be None"
            )

        _buffer_infos.buffer_data += src.read(src.remaining())
        return None
