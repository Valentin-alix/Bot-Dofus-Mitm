import logging
from network.utils import get_local_ip

from models.data import Data
from models.message import Message
from network.utils import NetworkMessage
from network.parser import MessageRawDataParser
from scapy.all import Packet, Raw, sniff
from scapy.layers.inet import IP

logger = logging.getLogger(__name__)


FILTER_DOFUS = "tcp port 5555"

MESSAGE_SIZE_ASYNC_THRESHOLD = 300 * 1024


class Sniffer:
    def __init__(self):
        self._raw_parser: MessageRawDataParser = MessageRawDataParser()
        self._splitted_packet = False
        self._static_header: int
        self._splitted_packet_id = None
        self._splitted_packet_length = None
        self._async_network_data_container_message = Data()
        self._buffer = Data()
        self._ip_local = get_local_ip()

    def launch_sniffer(self) -> None:
        logger.info("Launching Sniffer")
        sniff(prn=self.on_receive, store=False, filter=FILTER_DOFUS)

    def on_receive(self, packet: Packet):
        if Raw in packet:
            src_ip = packet[IP].src
            # TODO Differentiate from client and not
            if src_ip != self._ip_local:
                data = Data(packet[Raw].load)
                logger.info(f"Received Packet : Raw : {str(data)} \n src IP : {src_ip}")
                self.receive(data)

    def receive(self, data: Data):
        msg = None
        if data.remaining() > 0:
            msg = self.low_receive(data)
            while msg is not None:
                msg = self.low_receive(data)

    def low_receive(self, src: Data) -> Message:
        msg = None
        static_header = 0
        message_id = 0
        message_length = 0
        if not self._splitted_packet:
            if src.remaining() < 2:
                return None

            static_header = int(src.readUnsignedShort())

            # if from_client:
            #     src.readUnsignedInt()

            message_id = self.get_message_id(static_header)
            message_length = self.read_message_length(static_header, src)

            if (
                MessageRawDataParser().get_message_type_from_id(message_id)
                == "NetworkDataContainerMessage"
            ):
                logger.info("Received NetworkDataContainerMessage")
                if src.remaining() >= message_length:
                    content_len = int(src.readVarInt())
                    buffer_network_data_container_message = Data(src.read(content_len))
                    buffer_network_data_container_message.uncompress()
                    self._async_network_data_container_message = Data()
                    logger.info("Uncompressing NetworkDataContainerMessage")
                    return self.low_receive(buffer_network_data_container_message)

                self._async_network_data_container_message += src
                return None

            if src.remaining() >= (static_header & NetworkMessage.BIT_MASK):
                if src.remaining() >= message_length:
                    msg = self._raw_parser.parse(src, message_id, message_length)
                    return msg

                self._static_header = -1
                self._splitted_packet_length = message_length
                self._splitted_packet_id = message_id
                self._splitted_packet = True
                self._buffer = Data(src.read(src.remaining()))
                return None

            self._static_header = static_header
            self._splitted_packet_length = message_length
            self._splitted_packet_id = message_id
            self._splitted_packet = True
            return None

        if self._static_header != -1:
            self._splitted_packet_length = self.read_message_length(
                self._static_header, src
            )
            self._static_header = -1

        if src.remaining() + len(self._buffer) >= self._splitted_packet_length:
            self._buffer += src.read(self._splitted_packet_length - len(self._buffer))
            self._buffer.pos = 0

            msg = self._raw_parser.parse(
                self._buffer,
                self._splitted_packet_id,
                self._splitted_packet_length,
            )

            self._splitted_packet = False
            self._buffer = Data()
            return msg

        self._buffer += src.read(src.remaining())
        return None

    def get_message_id(self, first_octet):
        return first_octet >> NetworkMessage.BIT_RIGHT_SHIFT_LEN_PACKET_ID

    def read_message_length(self, static_header, src: Data):
        byte_len_dynamic_header = int(static_header & NetworkMessage.BIT_MASK)
        message_length = 0

        if byte_len_dynamic_header == 1:
            message_length = int(src.readUnsignedByte())
        elif byte_len_dynamic_header == 2:
            message_length = int(src.readUnsignedShort())
        elif byte_len_dynamic_header == 3:
            message_length = int(
                ((src.readByte() & 255) << 16)
                + ((src.readByte() & 255) << 8)
                + (src.readByte() & 255)
            )
        return message_length
