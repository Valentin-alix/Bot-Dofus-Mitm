from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameFightJoinRequestMessage:
	def __init__(self, fighterId:float, fightId:int):
		self.fighterId=fighterId
		self.fightId=fightId