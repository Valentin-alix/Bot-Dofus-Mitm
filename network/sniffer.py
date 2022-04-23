import pyshark
from databases.database_management import DatabaseManagement
from models.data import Data
from network import deserialiser
from models.message import Message


class Sniffer:

    def __init__(self):
        self.__filter_dofus = 'tcp port 5555'
        self.__ip_dofus = '172.65.237.72'
        self.__buffer = Data()

    @property
    def filter_dofus(self) -> str:
        return self.__filter_dofus

    @property
    def ip_dofus(self) -> str:
        return self.__ip_dofus

    @property
    def buffer(self):
        return self.__buffer

    @buffer.setter
    def buffer(self, value):
        self.__buffer = value

    def launch_sniffer(self):
        capture = pyshark.LiveCapture(bpf_filter=self.filter_dofus)
        for packet in capture.sniff_continuously():
            try:
                if packet.ip.src == self.ip_dofus:
                    self.buffer += bytearray.fromhex(packet.data.data)
                    self.on_receive()
                else:
                    pass
            except AttributeError:
                pass

    def on_receive(self):
        while True:
            try:
                header = self.buffer.readUnsignedShort()
                message_id = header >> 2

                len_data = int.from_bytes(self.buffer.read(header & 3), "big")
                if len_data > 5000 or not DatabaseManagement().select_message_by_id(message_id):
                    self.buffer.__init__()
                    break

                data = Data(self.buffer.read(len_data))
                message = Message(message_id, data)
                deserialiser.interpretation(message)
                del self.buffer.data[:2 + (header & 3) + len_data]
                self.buffer.reset_pos()
            except IndexError:
                self.buffer.reset_pos()
                break
