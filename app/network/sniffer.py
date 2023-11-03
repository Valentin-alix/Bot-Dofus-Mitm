import logging
from queue import Queue
from threading import Event
from typing import Optional

from network.models.data import BufferInfos, Data
from network.models.message import Message, ParsedMessage
from network.parser import MessageRawDataParser
from network.utils import FILTER_DOFUS, get_local_ip
from scapy.all import Packet, Raw, sniff
from scapy.layers.inet import IP

logger = logging.getLogger(__name__)


class Sniffer:
    def __init__(
        self,
        queue_handler_message: Optional[Queue[ParsedMessage]] = None,
        event_play_sniffer: Optional[Event] = None,
        capture_path: Optional[str] = None,
    ):
        self.raw_parser = MessageRawDataParser(
            queue_handler_message=queue_handler_message, on_error_callback=self.on_error
        )
        self.event_play_sniffer = event_play_sniffer
        self.not_completed_message_number: int = 0
        self.capture_path: str | None = capture_path
        self.buffer_infos_from_server = BufferInfos()
        self.buffer_infos_from_client = BufferInfos()
        self.ip_local = get_local_ip()

    def launch_sniffer(self) -> None:
        if self.capture_path:
            sniff(prn=self.on_receive, offline=self.capture_path)
        else:
            while True:
                if self.event_play_sniffer is None or self.event_play_sniffer.wait():
                    sniff(
                        prn=self.on_receive,
                        store=False,
                        filter=FILTER_DOFUS,
                        stop_filter=lambda _: self.event_play_sniffer is None
                        or not self.event_play_sniffer.is_set(),
                    )

    def on_receive(self, packet: Packet):
        if Raw in packet:
            src_ip: int = packet[IP].src
            data = Data(packet[Raw].load)
            logger.info(f"Received Packet : Raw : {str(data)} \n src IP : {src_ip}")
            self.receive(data, src_ip == self.ip_local)

    def receive(self, data: Data, from_client: bool):
        if data.remaining() > 0:
            buffer_infos = (
                self.buffer_infos_from_client
                if from_client
                else self.buffer_infos_from_server
            )
            msg = Message.from_raw(data, from_client, buffer_infos, self.on_error)
            while msg is not None:
                self.raw_parser.parse(msg, from_client)
                msg = Message.from_raw(data, from_client, buffer_infos, self.on_error)

    def on_error(self, _):
        self.not_completed_message_number += 1
