import socket
import pyshark

from assets.colors import Colors
from factory import reader
from models.data import Data


class Sniffer:

    def __init__(self):
        self.__filter_dofus = 'tcp port 5555 and len > 66'
        self.__ip_dofus = '172.65.237.72'
        self.__buffer = ''
        self.__network_interface = "\\Device\\NPF_{3CC6E476-ECB5-46EF-9768-419794EAE46A}"

    @property
    def filter_dofus(self):
        return self.__filter_dofus

    @property
    def ip_dofus(self):
        return self.__ip_dofus

    @property
    def buffer(self):
        return self.__buffer

    @property
    def network_interface(self):
        return self.__network_interface

    @buffer.setter
    def buffer(self, value):
        self.__buffer = value

    def reset_buffer(self):
        self.__buffer = ''

    def launch_sniffer(self):
        capture = pyshark.LiveCapture(interface=self.network_interface,
                                      bpf_filter=self.filter_dofus)
        for packet in capture.sniff_continuously():
            try:
                if packet.ip.src == socket.gethostbyname(self.ip_dofus):
                    self.buffer += packet.data.data
                    if len(self.buffer) >= 4:
                        self.extract_dofus_message()
            except AttributeError:
                pass

    @staticmethod
    def calcul_size(data: str):

        if len(data) == 0 or len(data) < 4:
            return 0
        size_of_size = int(bin(int(data[:4], 16))[2::][-2:], 2) * 2
        if size_of_size == 0 or len(data) == 4:
            return 4
        size = int(data[4:4 + size_of_size], 16) * 2
        total_size = 4 + size_of_size + size

        return total_size

    def extract_dofus_message(self):
        if len(self.buffer) < 4:
            return
        if self.calcul_size(self.buffer) >= 19998:
            print(f" {Colors.FAIL}Reset Buffer : {self.buffer}{Colors.RESET}")
            self.reset_buffer()
            return
        if self.calcul_size(self.buffer) > len(self.buffer):
            return

        while (self.calcul_size(self.buffer) <= len(self.buffer)) and len(self.buffer) >= 4:
            data_object = Data(bytearray.fromhex(self.buffer[:Sniffer.calcul_size(self.buffer)]))
            reader.interpretation(data_object)
            self.buffer = self.buffer[self.calcul_size(self.buffer):]
