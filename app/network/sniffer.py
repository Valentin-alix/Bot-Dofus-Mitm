import logging
from typing import Optional

from scapy.all import Packet, Raw, sniff
from scapy.layers.inet import IP

from app.network.models.data import BufferInfos, Data
from app.network.models.message import Message
from app.network.parser import MessageRawDataParser
from app.network.utils import get_local_ip
from app.types_ import FILTER_DOFUS, BotInfo

logger = logging.getLogger(__name__)


class Sniffer:
    def __init__(
            self,
            bot_info: BotInfo | None = None,
            capture_path: Optional[str] = None,
    ):
        self.bot_info = bot_info
        self.raw_parser = MessageRawDataParser(
            bot_info=bot_info,
            on_error_callback=self.on_error,
        )
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
                if (
                        self.bot_info is None
                        or self.bot_info.sniffer_info.is_playing_event.wait()
                ):
                    sniff(
                        prn=self.on_receive,
                        store=False,
                        filter=FILTER_DOFUS,
                        stop_filter=lambda _: self.bot_info is None
                                              or not self.bot_info.sniffer_info.is_playing_event.is_set(),
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
            buffer_infos.data += data
            msg = Message.from_raw(from_client, buffer_infos, self.on_error)
            while msg is not None:
                self.raw_parser.parse(msg, from_client)
                msg = Message.from_raw(from_client, buffer_infos, self.on_error)

    def on_error(self, _):
        self.not_completed_message_number += 1
