from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class HaapiCancelBidRequestMessage:
	def __init__(self, id:int, type:int):
		self.id=id
		self.type=type