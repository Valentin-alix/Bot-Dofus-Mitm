from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ExchangeReadyMessage:
	def __init__(self, ready:bool, step:int):
		self.ready=ready
		self.step=step