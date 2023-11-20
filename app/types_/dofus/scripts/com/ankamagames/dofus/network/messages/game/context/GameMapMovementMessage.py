from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameMapMovementMessage:
	def __init__(self, keyMovements:list[int], forcedDirection:int, actorId:float):
		self.keyMovements=keyMovements
		self.forcedDirection=forcedDirection
		self.actorId=actorId