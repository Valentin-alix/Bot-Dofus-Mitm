from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ExchangeStoppedMessage:
	def __init__(self, id:int):
		self.id=id