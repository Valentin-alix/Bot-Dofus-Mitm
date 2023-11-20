from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameFightOptionStateUpdateMessage:
	def __init__(self, fightId:int, teamId:int, option:int, state:bool):
		self.fightId=fightId
		self.teamId=teamId
		self.option=option
		self.state=state