from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class MapCoordinates:
	def __init__(self, worldX:int, worldY:int):
		self.worldX=worldX
		self.worldY=worldY