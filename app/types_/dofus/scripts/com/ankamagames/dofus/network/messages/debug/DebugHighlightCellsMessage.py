from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class DebugHighlightCellsMessage:
	def __init__(self, color:float, cells:list[int]):
		self.color=color
		self.cells=cells