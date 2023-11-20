from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameRolePlayAggressionMessage:
	def __init__(self, attackerId:int, defenderId:int):
		self.attackerId=attackerId
		self.defenderId=defenderId