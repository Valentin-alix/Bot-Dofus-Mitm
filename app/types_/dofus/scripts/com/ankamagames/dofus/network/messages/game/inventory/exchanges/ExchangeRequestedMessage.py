from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ExchangeRequestedMessage:
	def __init__(self, exchangeType:int):
		self.exchangeType=exchangeType