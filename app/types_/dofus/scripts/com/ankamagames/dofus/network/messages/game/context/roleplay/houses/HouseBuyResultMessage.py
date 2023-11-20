from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class HouseBuyResultMessage:
	def __init__(self, houseId:int, instanceId:int, realPrice:int):
		self.houseId=houseId
		self.instanceId=instanceId
		self.realPrice=realPrice