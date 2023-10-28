import logging
import socket
import struct
import time
import traceback
from enum import Enum

from database import execute_sql
from models.data import Data
from network.parser import MessageRawDataParser
from scapy.all import IPField, Packet, Raw, sniff
from scapy.layers.inet import IP

logger = logging.getLogger(__name__)


FILTER_DOFUS = "tcp port 5555"


class NetworkMessage:
    BIT_RIGHT_SHIFT_LEN_PACKET_ID = 2
    BIT_MASK = 3


class Sniffer:
    def __init__(self, id=""):
        self._id = id
        self._rawParser: MessageRawDataParser = MessageRawDataParser()
        self._handler = None
        self._splittedPacket = False
        self._staticHeader: int
        self._splittedPacketId = None
        self._splittedPacketLength = None
        self._inputBuffer: Data = Data()
        self._input = Data()

    def launch_sniffer(self) -> None:
        logger.info("Launching Sniffer")
        sniff(prn=lambda packet: self.receive(packet), store=False, filter=FILTER_DOFUS)

    def receive(self, input: Packet):
        if Raw in input:
            src_ip = input[IP].src
            input = Data(input[Raw].load)
            logger.info(f"Received Packet : {str(input)} with src IP : {src_ip}")
            msg = None
            if input.remaining() > 0:
                msg = self.low_receive(input)
                while msg:
                    msg = self.low_receive(input)

    def low_receive(self, data: Data):
        msg = None
        staticHeader = 0
        messageId = 0
        messageLength = 0
        if not self._splittedPacket:
            if data.remaining() < 2:
                return None
            staticHeader = data.readUnsignedShort()
            messageId = self.get_message_id(staticHeader)

            if data.remaining() >= (staticHeader & NetworkMessage.BIT_MASK):
                messageLength = self.read_message_length(staticHeader, data)
                if data.remaining() >= messageLength:
                    msg = self._rawParser.parse(data, messageId, messageLength)
                    return msg

                self._staticHeader = -1
                self._splittedPacketLength = messageLength
                self._splittedPacketId = messageId
                self._splittedPacket = True

                self._inputBuffer = Data(data.read(data.remaining()))
                return None

            self._staticHeader = staticHeader
            self._splittedPacketLength = messageLength
            self._splittedPacketId = messageId
            self._splittedPacket = True
            return None

        if self._staticHeader != -1:
            self._splittedPacketLength = self.read_message_length(
                self._staticHeader, data
            )
            self._staticHeader = -1

        if data.remaining() + len(self._inputBuffer) >= self._splittedPacketLength:
            self._inputBuffer += data.read(
                self._splittedPacketLength - len(self._inputBuffer)
            )
            self._inputBuffer.pos = 0
            msg = self._rawParser.parse(
                self._inputBuffer,
                self._splittedPacketId,
                self._splittedPacketLength,
            )

            self._splittedPacket = False
            self._inputBuffer = Data()
            return msg

        self._inputBuffer += data.read(data.remaining())
        return None

    def get_message_id(self, first_octet):
        return first_octet >> NetworkMessage.BIT_RIGHT_SHIFT_LEN_PACKET_ID

    def read_message_length(self, static_header, src):
        byteLenDynamicHeader = int(static_header & NetworkMessage.BIT_MASK)
        messageLength = 0

        if byteLenDynamicHeader == 1:
            messageLength = int(src.readUnsignedByte())
        elif byteLenDynamicHeader == 2:
            messageLength = int(src.readUnsignedShort())
        elif byteLenDynamicHeader == 3:
            messageLength = int(
                ((src.readByte() & 255) << 16)
                + ((src.readByte() & 255) << 8)
                + (src.readByte() & 255)
            )
        logger.info(f"len : {messageLength}")
        return messageLength
