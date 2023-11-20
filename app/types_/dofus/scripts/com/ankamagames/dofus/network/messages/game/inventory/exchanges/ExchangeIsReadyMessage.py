from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ExchangeIsReadyMessage:
	def __init__(self, id:float, ready:bool):
		self.id=id
		self.ready=ready