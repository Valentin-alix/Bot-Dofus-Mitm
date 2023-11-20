from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class UpdateLifePointsMessage:
	def __init__(self, lifePoints:int, maxLifePoints:int):
		self.lifePoints=lifePoints
		self.maxLifePoints=maxLifePoints