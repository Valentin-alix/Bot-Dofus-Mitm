from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class AbstractFightTeamInformations:
	def __init__(self, teamId:int, leaderId:float, teamSide:int, teamTypeId:int, nbWaves:int):
		self.teamId=teamId
		self.leaderId=leaderId
		self.teamSide=teamSide
		self.teamTypeId=teamTypeId
		self.nbWaves=nbWaves