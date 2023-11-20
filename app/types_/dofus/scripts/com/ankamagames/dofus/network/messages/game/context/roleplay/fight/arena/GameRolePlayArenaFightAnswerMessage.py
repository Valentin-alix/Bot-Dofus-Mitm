from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameRolePlayArenaFightAnswerMessage:
	def __init__(self, fightId:int, accept:bool):
		self.fightId=fightId
		self.accept=accept