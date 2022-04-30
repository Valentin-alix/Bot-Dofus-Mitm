import unittest

import pyshark

from bot.network.sniffer import Sniffer


class TestSniffer(unittest.TestCase):
    def setUp(self) -> None:
        self.file = "test_capture.pcap"

    def test_no_exception(self):
        capture = pyshark.FileCapture(f"ressources/{self.file}", display_filter=Sniffer.FILTER_DOFUS)
        for packet in capture:
            print(packet)
        capture.close()
