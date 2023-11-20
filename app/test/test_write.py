import unittest

from app.network.protocol import protocol


class TestPriceQuantity(unittest.TestCase):
    def test_object_move_price(self):
        data = protocol.write("ExchangeObjectMovePricedMessage", {
            "__type__": "ExchangeObjectMovePricedMessage",
            "objectUID": 289,
            "price": 123,
            "quantity": 100,
        }, random_hash=False)
        print(data)
