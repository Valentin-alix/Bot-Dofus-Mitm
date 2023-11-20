from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class PaddockRemoveItemRequestMessage:
	def __init__(self, cellId:int):
		self.cellId=cellId