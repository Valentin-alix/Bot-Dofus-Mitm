import logging
import socket
import threading

import pyshark
from bot.databases.database import Database
from bot.factory import action
from bot.models.data import Data
from bot.models.message import Message
from bot.network import deserialiser


def get_local_ip() -> str:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        ip_local = s.getsockname()[0]
    except Exception:
        ip_local = '127.0.0.1'
    finally:
        s.close()
    return ip_local


class Sniffer:
    FILTER_DOFUS: str = 'tcp port 5555'
    IP_LOCALE = get_local_ip()

    def __init__(self) -> None:
        self.__buffer_client: Data = Data()
        self.__buffer_server: Data = Data()

    @property
    def buffer_client(self) -> Data:
        return self.__buffer_client

    @property
    def buffer_server(self) -> Data:
        return self.__buffer_server

    @buffer_client.setter
    def buffer_client(self, value) -> None:
        self.__buffer_client = value

    @buffer_server.setter
    def buffer_server(self, value) -> None:
        self.__buffer_server = value

    def launch_sniffer(self) -> None:
        capture = pyshark.LiveCapture(bpf_filter=self.FILTER_DOFUS)
        for packet in capture.sniff_continuously():
            self.on_receive(packet)

    def on_receive(self, packet) -> None:
        try:
            if packet.ip.src == self.IP_LOCALE:
                try:
                    logging.warning(f"tcp segment : {packet.tcp.segment_data}")
                    data: str = str(packet.tcp.segment_data).replace(":", "")
                    self.buffer_client += bytearray.fromhex(data)
                    self.from_raw(self.buffer_client, True)
                    return
                except AttributeError:
                    pass
                logging.info(f"Data receive : {packet.data.data}")
                self.buffer_client += bytearray.fromhex(packet.data.data)
                self.from_raw(self.buffer_client, True)
            else:
                try:
                    logging.warning(f"tcp segment : {packet.tcp.segment_data}")
                    data = str(packet.tcp.segment_data).replace(":", "")
                    self.buffer_server += bytearray.fromhex(data)
                    self.from_raw(self.buffer_server, False)
                    return
                except AttributeError:
                    pass
                logging.info(f"Data receive : {packet.data.data}")
                self.buffer_server += bytearray.fromhex(packet.data.data)
                self.from_raw(self.buffer_server, False)
        except AttributeError:
            pass

    @staticmethod
    def from_raw(buffer: Data, from_client: bool) -> None:
        while True:
            try:
                logging.info(f"{from_client} | Trying to extract these data : {buffer}")

                header = buffer.readUnsignedShort()
                message_id = header >> 2

                if from_client:
                    buffer.readUnsignedInt()

                if id == 2:
                    logging.info("Message is NetworkDataContainerMessage! Uncompressing...")
                    new_buffer = Data(buffer.readByteArray())
                    new_buffer.uncompress()
                    Sniffer.from_raw(new_buffer, from_client)
                    break

                len_data = int.from_bytes(buffer.read(header & 3), "big")

                if not Database().select_message_by_id(message_id):
                    logging.error("Can't get corresponding message to id")
                    print("Error Sniffer, réinitialisation buffer...")
                    buffer.__init__()
                    break
                if Database().select_message_by_id(message_id) == "ExchangeReadyMessage":
                    action.waiting_click = False
                logging.info(f"Message :{Database().select_message_by_id(message_id)}")
                data = Data(buffer.read(len_data))
                message = Message(message_id, data)
                interpretation_thread = threading.Thread(target=deserialiser.interpretation, args=(message,))
                interpretation_thread.start()
                buffer.end()
            except IndexError:
                buffer.reset_pos()
                break
