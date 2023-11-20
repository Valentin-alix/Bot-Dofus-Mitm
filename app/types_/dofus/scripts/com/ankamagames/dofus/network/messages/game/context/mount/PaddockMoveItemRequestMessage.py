from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class PaddockMoveItemRequestMessage:
	def __init__(self, oldCellId:int, newCellId:int):
		self.oldCellId=oldCellId
		self.newCellId=newCellId