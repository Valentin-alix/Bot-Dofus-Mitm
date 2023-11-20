from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ClientUIOpenedMessage:
	def __init__(self, type:int):
		self.type=type