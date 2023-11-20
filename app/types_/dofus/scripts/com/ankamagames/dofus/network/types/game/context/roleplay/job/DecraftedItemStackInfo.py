from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class DecraftedItemStackInfo:
	def __init__(self, objectUID:int, bonusMin:float, bonusMax:float, runesId:list[int], runesQty:list[int]):
		self.objectUID=objectUID
		self.bonusMin=bonusMin
		self.bonusMax=bonusMax
		self.runesId=runesId
		self.runesQty=runesQty