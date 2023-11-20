from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameRolePlayMonsterNotAngryAtPlayerMessage:
	def __init__(self, playerId:int, monsterGroupId:float):
		self.playerId=playerId
		self.monsterGroupId=monsterGroupId