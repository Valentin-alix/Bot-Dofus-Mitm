from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ExchangeBidHouseTypeMessage:
	def __init__(self, type:int, follow:bool):
		self.type=type
		self.follow=follow