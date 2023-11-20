from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class NamedPartyTeam:
	def __init__(self, teamId:int, partyName:str):
		self.teamId=teamId
		self.partyName=partyName