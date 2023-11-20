from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameFightRemoveTeamMemberMessage:
	def __init__(self, fightId:int, teamId:int, charId:float):
		self.fightId=fightId
		self.teamId=teamId
		self.charId=charId