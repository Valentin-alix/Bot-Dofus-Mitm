import unittest

from factory.reader import Reader
from models import sniffer
from models.sniffer import Sniffer


class TestPacket(unittest.TestCase):
    packet_test1 = "1ed114000401f901eb01de01c20001425c6533800900002768"
    packet_test2 = "4dad0da480b8a6990eddee1fb801000191b52a41a9580c040000000020363439616534353163613333656335336262636263633333626563663135663471b90a4277f939085ca000003c "
    packet_test3 = "01059da731000753205020512052563a00ffffff0b00951f170d61424a1db9801200001d00021703d903000000000001"
    packet_test4 = "4dad0da480b8a6990eddee1fb801000191b52a41a9580c040000000020363439616534353163613333656335336262636263633333626563663135663471b90a4277f949cb879000003c5db1020000"
    packet_test5 = "2768"
    packet_test6 = "5d3d6505000a415620efbfbc2031396d62337aec0008397267677862306342616dcde004800000084b68656e7368696e0000084a628d0001003fd6960100060873a403640873a0036408730aa90104188516790065041883160000bffc0b0873c11600c591d22101"

    def test_size(self):
        self.assertEqual(Sniffer.calcul_size(self.packet_test1), 46)
        self.assertEqual(Sniffer.calcul_size(self.packet_test4), 32)
        self.assertEqual(Sniffer.calcul_size(self.packet_test5), 4)
        self.assertEqual(Sniffer.calcul_size(self.packet_test6), 208)

    def test_recup_id(self):
        self.assertEqual(Reader.recuperation_id(self.packet_test1), 1972)