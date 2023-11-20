from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameRolePlayArenaFightPropositionMessage:
	def __init__(self, fightId:int, alliesId:list[float], duration:int):
		self.fightId=fightId
		self.alliesId=alliesId
		self.duration=duration