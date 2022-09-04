import logging
from queue import Queue
import socket
from threading import Event

import pyshark
from databases.database import *

from models.data import Data
from network.message import Message

FILTER_DOFUS: str = 'tcp port 5555'
logger = logging.getLogger(__name__)


def get_local_ip() -> str:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        ip_local = s.getsockname()[0]
        logger.info(msg=f"Local ip = {ip_local}")
    except Exception as e:
        logger.error(msg="Exception on get local ip")
        ip_local = '127.0.0.1'
    finally:
        s.close()
    return ip_local


class Sniffer:
    def __init__(self, queue_actual_item: Queue, event_ready: Event, event_move: Event, event_is_playing: Event):
        self.queue_actual_item: Queue = queue_actual_item
        self.event_ready: Event = event_ready
        self.event_move: Event = event_move
        self.event_is_playing: Event = event_is_playing
        self.buffer_client: Data = Data()
        self.buffer_server: Data = Data()
        self.ip_local: str = get_local_ip()

    def launch_sniffer(self) -> None:
        logger.info("Launching Sniffer")
        capture = pyshark.LiveCapture(bpf_filter=FILTER_DOFUS)
        for packet in capture.sniff_continuously():
            self.on_receive(packet)

    def on_receive(self, packet) -> None:
        if hasattr(packet, 'tcp') and hasattr(packet.tcp, 'payload'):
            packet_data = packet.tcp.payload.replace(":", "")
            if packet.ip.src == self.ip_local:
                logger.info(f"Data receive : {packet_data}")
                self.buffer_client += bytearray.fromhex(packet_data)
                self.from_raw(self.buffer_client, True)
            else:
                logger.info(f"Data receive : {packet_data}")
                self.buffer_server += bytearray.fromhex(packet_data)
                self.from_raw(self.buffer_server, False)

    def from_raw(self, buffer: Data, from_client: bool) -> None:
        while True:
            try:
                logger.info(
                    f"{from_client} | Trying to extract these data : {buffer}")

                header = buffer.readUnsignedShort()
                message_id = header >> 2

                if from_client:
                    buffer.readUnsignedInt()

                if id == 2:
                    logger.info(
                        "Message is NetworkDataContainerMessage! Uncompressing...")
                    new_buffer = Data(buffer.readByteArray())
                    new_buffer.uncompress()
                    self.from_raw(new_buffer, from_client)
                    break

                len_data = int.from_bytes(buffer.read(header & 3), "big")
                if not select_message_by_protocol_id(message_id):
                    logger.error(
                        "Can't get corresponding message to id, reinitializing buffer")
                    buffer.__init__()
                    break
                logger.info(
                    f"Message :{select_message_by_protocol_id(message_id)}")
                data = Data(buffer.read(len_data))
                message = Message(message_id, data)

                logger.info(select_message_by_protocol_id(message_id))

                if self.event_is_playing.is_set():
                    if select_message_by_protocol_id(message_id) == "ExchangeReadyMessage":
                        logger.info("set ready message")
                        self.event_ready.set()
                    elif select_message_by_protocol_id(message_id) == "ExchangeObjectMoveMessage":
                        logger.info("set move message")
                        self.event_move.set()
                message.event(self.queue_actual_item, self.event_is_playing)
                buffer.end()
            except IndexError:
                buffer.reset_pos()
                break
