import threading

import pyshark

from databases.database import Database
from factory import action
from models.data import Data
from models.message import Message
from network import deserialiser


class Sniffer:
    FILTER_DOFUS: str = 'tcp port 5555'
    IP_LOCALE: str = '192.168.1.21'

    def __init__(self):
        self.__buffer_client = Data()
        self.__buffer_server = Data()

    @property
    def buffer_client(self) -> Data:
        return self.__buffer_client

    @buffer_client.setter
    def buffer_client(self, value):
        self.__buffer_client = value

    @property
    def buffer_server(self) -> Data:
        return self.__buffer_server

    @buffer_server.setter
    def buffer_server(self, value):
        self.__buffer_server = value

    def launch_sniffer(self):
        capture = pyshark.LiveCapture(bpf_filter=self.FILTER_DOFUS)
        for packet in capture.sniff_continuously():
            try:
                print(packet.data.data)
                if packet.ip.src == self.IP_LOCALE:
                    self.buffer_client += bytearray.fromhex(packet.data.data)
                    self.on_receive(self.buffer_client, True)
                else:
                    self.buffer_server += bytearray.fromhex(packet.data.data)
                    self.on_receive(self.buffer_server, False)
            except AttributeError:
                pass

    @staticmethod
    def on_receive(buffer: Data, from_client: bool):
        while True:
            try:
                header = buffer.readUnsignedShort()
                message_id = header >> 2

                if from_client:
                    buffer.readUnsignedInt()

                if id == 2:
                    print("Message is NetworkDataContainerMessage! Uncompressing...")
                    new_buffer = Data(buffer.readByteArray())
                    new_buffer.uncompress()
                    Sniffer.on_receive(new_buffer, from_client)
                    break

                len_data = int.from_bytes(buffer.read(header & 3), "big")

                if not Database().select_message_by_id(message_id):
                    print("stop")
                    exit()
                if Database().select_message_by_id(message_id) == "ExchangeReadyMessage":
                    action.waiting_click = False
                print(Database().select_message_by_id(message_id))
                data = Data(buffer.read(len_data))
                message = Message(message_id, data)

                interpretation_thread = threading.Thread(target=deserialiser.interpretation, args=(message,))
                interpretation_thread.start()

                buffer.end()

            except IndexError:
                buffer.reset_pos()
                break
