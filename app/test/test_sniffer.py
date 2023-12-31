import logging.config
import os
import unittest
from pathlib import Path

import app.network.sniffer as sniffer
from app.logs.config import LOGGING_CONFIG

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)


class TestSniffer(unittest.TestCase):
    def setUp(self) -> None:
        self.sniffer = sniffer.Sniffer()

    def test_from_server(self):
        self.sniffer.capture_path = os.path.join(
            Path(__file__).parent, "fixtures", "from_server.pcap"
        )
        self.sniffer.launch_sniffer()
        logger.warning(f"not_completed: {self.sniffer.not_completed_message_number}")
        assert self.sniffer.not_completed_message_number <= 1

    def test_from_client_and_from_server(self):
        self.sniffer.capture_path = os.path.join(
            Path(__file__).parent, "fixtures", "from_client_and_from_server.pcap"
        )
        self.sniffer.launch_sniffer()
        logger.warning(f"not_completed: {self.sniffer.not_completed_message_number}")
        assert self.sniffer.not_completed_message_number <= 0

    def test_from_client_and_from_server2(self):
        self.sniffer.capture_path = os.path.join(
            Path(__file__).parent, "fixtures", "from_client_and_from_server2.pcap"
        )
        self.sniffer.launch_sniffer()
        logger.warning(f"not_completed: {self.sniffer.not_completed_message_number}")
        assert self.sniffer.not_completed_message_number <= 3


if __name__ == "__main__":
    unittest.main()
