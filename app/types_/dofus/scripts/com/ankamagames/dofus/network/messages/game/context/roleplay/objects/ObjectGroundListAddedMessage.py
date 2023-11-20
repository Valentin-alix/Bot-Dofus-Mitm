from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ObjectGroundListAddedMessage:
	def __init__(self, cells:list[int], referenceIds:list[int]):
		self.cells=cells
		self.referenceIds=referenceIds