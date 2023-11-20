from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class MonsterBoosts:
	def __init__(self, id:int, xpBoost:int, dropBoost:int):
		self.id=id
		self.xpBoost=xpBoost
		self.dropBoost=dropBoost