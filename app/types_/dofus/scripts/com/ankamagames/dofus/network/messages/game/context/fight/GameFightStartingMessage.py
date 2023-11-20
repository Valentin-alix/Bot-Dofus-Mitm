from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameFightStartingMessage:
	def __init__(self, fightType:int, fightId:int, attackerId:float, defenderId:float, containsBoss:bool, monsters:list[int]):
		self.fightType=fightType
		self.fightId=fightId
		self.attackerId=attackerId
		self.defenderId=defenderId
		self.containsBoss=containsBoss
		self.monsters=monsters