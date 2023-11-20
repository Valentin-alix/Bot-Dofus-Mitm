from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameRolePlayMonsterAngryAtPlayerMessage:
	def __init__(self, playerId:int, monsterGroupId:float, angryStartTime:float, attackTime:float):
		self.playerId=playerId
		self.monsterGroupId=monsterGroupId
		self.angryStartTime=angryStartTime
		self.attackTime=attackTime