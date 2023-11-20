from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ObtainedItemMessage:
	def __init__(self, genericId:int, baseQuantity:int):
		self.genericId=genericId
		self.baseQuantity=baseQuantity