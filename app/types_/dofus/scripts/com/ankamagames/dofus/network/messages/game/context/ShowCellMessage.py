from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ShowCellMessage:
	def __init__(self, sourceId:float, cellId:int):
		self.sourceId=sourceId
		self.cellId=cellId