from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class PaddockToSellFilterMessage:
	def __init__(self, areaId:int, atLeastNbMount:int, atLeastNbMachine:int, maxPrice:int, orderBy:int):
		self.areaId=areaId
		self.atLeastNbMount=atLeastNbMount
		self.atLeastNbMachine=atLeastNbMachine
		self.maxPrice=maxPrice
		self.orderBy=orderBy