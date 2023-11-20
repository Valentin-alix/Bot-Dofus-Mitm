from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ExchangeBidHouseBuyResultMessage:
	def __init__(self, uid:int, bought:bool):
		self.uid=uid
		self.bought=bought