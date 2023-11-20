from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ObjectAveragePricesMessage:
	def __init__(self, ids:list[int], avgPrices:list[int]):
		self.ids=ids
		self.avgPrices=avgPrices