from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameFightPlacementPossiblePositionsMessage:
	def __init__(self, positionsForChallengers:list[int], positionsForDefenders:list[int], teamNumber:int):
		self.positionsForChallengers=positionsForChallengers
		self.positionsForDefenders=positionsForDefenders
		self.teamNumber=teamNumber