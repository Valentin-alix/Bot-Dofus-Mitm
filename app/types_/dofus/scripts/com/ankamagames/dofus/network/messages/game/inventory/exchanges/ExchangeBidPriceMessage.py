from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ExchangeBidPriceMessage:
	def __init__(self, genericId:int, averagePrice:int):
		self.genericId=genericId
		self.averagePrice=averagePrice