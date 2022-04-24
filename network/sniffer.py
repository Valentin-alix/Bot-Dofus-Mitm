import pyshark
from pyshark.capture.capture import TSharkCrashException

from databases.database_management import DatabaseManagement
from models.data import Data
from network import deserialiser
from models.message import Message


class Sniffer:
    FILTER_DOFUS = 'tcp port 5555'
    IP_DOFUS = '172.65.237.72'

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
                if packet.ip.src == self.IP_DOFUS:
                    self.buffer_server += bytearray.fromhex(packet.data.data)
                    self.on_receive(self.buffer_server, False)
                else:
                    pass
                    '''self.buffer_client += bytearray.fromhex(packet.data.data)
                    self.on_receive(self.buffer_client, True)'''
            except AttributeError:
                pass

    @staticmethod
    def on_receive(buffer: Data(), from_client: bool):
        while True:
            try:
                header = buffer.readUnsignedShort()
                message_id = header >> 2

                '''if from_client:
                    buffer.readUnsignedInt()'''

                len_data = int.from_bytes(buffer.read(header & 3), "big")
                if len_data > 5000 or not DatabaseManagement().select_message_by_id(message_id):
                    buffer.__init__()
                    break

                data = Data(buffer.read(len_data))
                message = Message(message_id, data)

                deserialiser.interpretation(message)
                del buffer.data[:2 + (header & 3) + len_data]
                buffer.reset_pos()
            except IndexError:
                buffer.reset_pos()
                break
