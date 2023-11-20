from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameRolePlayArenaFighterStatusMessage:
	def __init__(self, fightId:int, playerId:int, accepted:bool):
		self.fightId=fightId
		self.playerId=playerId
		self.accepted=accepted