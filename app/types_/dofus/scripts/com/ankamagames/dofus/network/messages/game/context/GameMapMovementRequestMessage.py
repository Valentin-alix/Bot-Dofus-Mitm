from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameMapMovementRequestMessage:
	def __init__(self, keyMovements:list[int], mapId:float):
		self.keyMovements=keyMovements
		self.mapId=mapId