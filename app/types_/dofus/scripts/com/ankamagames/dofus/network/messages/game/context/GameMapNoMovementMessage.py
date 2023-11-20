from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameMapNoMovementMessage:
	def __init__(self, cellX:int, cellY:int):
		self.cellX=cellX
		self.cellY=cellY