from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ExchangeOkMultiCraftMessage:
	def __init__(self, initiatorId:int, otherId:int, role:int):
		self.initiatorId=initiatorId
		self.otherId=otherId
		self.role=role