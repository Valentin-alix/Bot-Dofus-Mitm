from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ExchangeWeightMessage:
	def __init__(self, currentWeight:int, maxWeight:int):
		self.currentWeight=currentWeight
		self.maxWeight=maxWeight