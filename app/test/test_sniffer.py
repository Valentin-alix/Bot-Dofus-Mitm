import logging
import logging.config
import unittest
from pathlib import Path
import os
from logs.config import LOGGING_CONFIG

from network.sniffer import Sniffer

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)


class TestSniffer(unittest.TestCase):
    def setUp(self) -> None:
        self.sniffer = Sniffer()

    def test_from_server(self):
        self.sniffer.capture_path = os.path.join(
            Path(__file__).parent, "fixtures", "from_server.pcap"
        )
        self.sniffer.launch_sniffer()
        assert self.sniffer.not_completed_message_number <= 2

    def test_from_client_and_from_server(self):
        self.sniffer.capture_path = os.path.join(
            Path(__file__).parent, "fixtures", "from_client_and_from_server.pcap"
        )
        self.sniffer.launch_sniffer()
        assert self.sniffer.not_completed_message_number <= 4

    def test_from_client_and_from_server2(self):
        self.sniffer.capture_path = os.path.join(
            Path(__file__).parent, "fixtures", "from_client_and_from_server2.pcap"
        )
        self.sniffer.launch_sniffer()
        assert self.sniffer.not_completed_message_number <= 27


if __name__ == "__main__":
    unittest.main()
