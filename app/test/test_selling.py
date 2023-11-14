import unittest

from app.modules.hdv.selling_hdv import SellingHdv


class TestPriceQuantity(unittest.TestCase):
    def test_unique(self):
        quantity, price = SellingHdv.get_price_and_quantity(1, [15, 149, 1699])
        assert quantity == 1
        assert price == 15

    def test_ten(self):
        quantity, price = SellingHdv.get_price_and_quantity(14, [15, 149, 1699])
        assert quantity == 10
        assert price == 149

    def test_hundred(self):
        quantity, price = SellingHdv.get_price_and_quantity(14564, [15, 149, 1699])
        assert quantity == 100
        assert price == 1699

    def test_mixin(self):
        quantity, price = SellingHdv.get_price_and_quantity(14564, [15, 149, 0])
        assert quantity == 100
        assert price == 1490

    def test_mixin2(self):
        quantity, price = SellingHdv.get_price_and_quantity(8, [0, 149, 0])
        assert quantity == 1
        assert price == 15

    def test_mixin3(self):
        quantity, price = SellingHdv.get_price_and_quantity(120, [1, 28, 3206])
        assert quantity == 100
        assert price == 3206
