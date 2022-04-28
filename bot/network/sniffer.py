import logging
import threading

import pyshark

from bot.databases.database import Database
from bot.factory import action
from bot.models.data import Data
from bot.models.message import Message
from bot.network import deserialiser


class Sniffer:
    FILTER_DOFUS: str = 'tcp port 5555'
    IP_LOCALE: str = '192.168.1.21'

    def __init__(self):
        self.__buffer_client: Data = Data()
        self.__buffer_server: Data = Data()
        self.__temp_buffer: Data = Data()
        self.__temp_buffer_from_local: bool = False

    @property
    def buffer_client(self) -> Data:
        return self.__buffer_client

    @property
    def buffer_server(self) -> Data:
        return self.__buffer_server

    @property
    def temp_buffer(self):
        return self.__temp_buffer

    @property
    def temp_buffer_from_local(self):
        return self.__temp_buffer_from_local

    @temp_buffer_from_local.setter
    def temp_buffer_from_local(self, value):
        self.__temp_buffer_from_local = value

    @temp_buffer.setter
    def temp_buffer(self, value):
        self.__temp_buffer = value

    @buffer_client.setter
    def buffer_client(self, value) -> None:
        self.__buffer_client = value

    @buffer_server.setter
    def buffer_server(self, value) -> None:
        self.__buffer_server = value

    def launch_sniffer(self) -> None:
        capture = pyshark.LiveCapture(bpf_filter=self.FILTER_DOFUS)
        for packet in capture.sniff_continuously():
            try:
                logging.info(f"Received_Packet : {packet.data.data}")
                if hasattr(packet[packet.transport_layer], 'analysis_lost_segment'):
                    logging.info("erreur lost segment")
                    self.temp_buffer = bytearray.fromhex(packet.data.data)
                    if packet.ip.src == self.IP_LOCALE:
                        self.temp_buffer_from_local = True
                        continue
                    else:
                        self.temp_buffer_from_local = False
                        continue

                try:
                    if hasattr(packet.tcp, 'segment_data'):
                        if packet.ip.src == self.IP_LOCALE:
                            self.buffer_client += str(packet.tcp.segment_data).replace(":", "")
                            if len(self.temp_buffer) != 0 and self.temp_buffer_from_local:
                                self.buffer_client += self.temp_buffer
                                self.temp_buffer.__init__()
                            self.on_receive(self.buffer_client, True)
                        else:
                            self.buffer_server += str(packet.tcp.segment_data).replace(":", "")
                            if len(self.temp_buffer) != 0 and not self.temp_buffer_from_local:
                                self.buffer_server += self.temp_buffer
                                self.temp_buffer.__init__()
                            self.on_receive(self.buffer_server, False)
                except AttributeError:
                    pass

                if packet.ip.src == self.IP_LOCALE:
                    self.buffer_client += bytearray.fromhex(packet.data.data)
                    if len(self.temp_buffer) != 0 and self.temp_buffer_from_local:
                        self.buffer_client += self.temp_buffer
                        self.temp_buffer.__init__()
                    self.on_receive(self.buffer_client, True)
                else:
                    self.buffer_server += bytearray.fromhex(packet.data.data)
                    if len(self.temp_buffer) != 0 and not self.temp_buffer_from_local:
                        self.buffer_server += self.temp_buffer
                        self.temp_buffer.__init__()
                    self.on_receive(self.buffer_server, False)
            except AttributeError:
                pass

    @staticmethod
    def on_receive(buffer: Data, from_client: bool) -> None:
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
                    Sniffer.on_receive(new_buffer, from_client)
                    break

                len_data = int.from_bytes(buffer.read(header & 3), "big")

                if not Database().select_message_by_id(message_id):
                    logging.error("Can't get corresponding message to id")
                    print("Error Sniffer")
                    exit()
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
