from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ExchangeBidHouseInListRemovedMessage:
	def __init__(self, itemUID:int, objectGID:int, objectType:int):
		self.itemUID=itemUID
		self.objectGID=objectGID
		self.objectType=objectType