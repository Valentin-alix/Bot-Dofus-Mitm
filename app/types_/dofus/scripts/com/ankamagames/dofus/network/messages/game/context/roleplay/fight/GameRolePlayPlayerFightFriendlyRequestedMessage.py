from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameRolePlayPlayerFightFriendlyRequestedMessage:
	def __init__(self, fightId:int, sourceId:int, targetId:int):
		self.fightId=fightId
		self.sourceId=sourceId
		self.targetId=targetId