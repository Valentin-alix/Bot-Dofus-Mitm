from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class EntityDispositionInformations:
	def __init__(self, cellId:int, direction:int):
		self.cellId=cellId
		self.direction=direction