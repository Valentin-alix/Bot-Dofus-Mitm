from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ExchangeWaitingResultMessage:
	def __init__(self, bwait:bool):
		self.bwait=bwait