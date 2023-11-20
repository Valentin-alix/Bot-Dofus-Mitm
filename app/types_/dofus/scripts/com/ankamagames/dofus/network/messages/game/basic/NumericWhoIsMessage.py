from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class NumericWhoIsMessage:
	def __init__(self, playerId:int, accountId:int):
		self.playerId=playerId
		self.accountId=accountId