from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class HouseSellRequestMessage:
	def __init__(self, instanceId:int, amount:int, forSale:bool):
		self.instanceId=instanceId
		self.amount=amount
		self.forSale=forSale