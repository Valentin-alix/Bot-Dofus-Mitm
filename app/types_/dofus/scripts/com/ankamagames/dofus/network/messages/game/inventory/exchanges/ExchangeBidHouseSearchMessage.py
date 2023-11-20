from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ExchangeBidHouseSearchMessage:
	def __init__(self, objectGID:int, follow:bool):
		self.objectGID=objectGID
		self.follow=follow