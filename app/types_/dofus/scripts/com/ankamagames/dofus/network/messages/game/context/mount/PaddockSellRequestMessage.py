from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class PaddockSellRequestMessage:
	def __init__(self, price:int, forSale:bool):
		self.price=price
		self.forSale=forSale