from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class FightStartingPositions:
	def __init__(self, positionsForChallengers:list[int], positionsForDefenders:list[int]):
		self.positionsForChallengers=positionsForChallengers
		self.positionsForDefenders=positionsForDefenders