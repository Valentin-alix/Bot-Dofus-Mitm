from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class HouseToSellFilterMessage:
	def __init__(self, areaId:int, atLeastNbRoom:int, atLeastNbChest:int, skillRequested:int, maxPrice:int, orderBy:int):
		self.areaId=areaId
		self.atLeastNbRoom=atLeastNbRoom
		self.atLeastNbChest=atLeastNbChest
		self.skillRequested=skillRequested
		self.maxPrice=maxPrice
		self.orderBy=orderBy