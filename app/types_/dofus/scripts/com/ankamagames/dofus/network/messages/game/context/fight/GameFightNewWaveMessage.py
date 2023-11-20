from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameFightNewWaveMessage:
	def __init__(self, id:int, teamId:int, nbTurnBeforeNextWave:int):
		self.id=id
		self.teamId=teamId
		self.nbTurnBeforeNextWave=nbTurnBeforeNextWave