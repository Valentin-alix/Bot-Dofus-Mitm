from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class DungeonPartyFinderPlayer:
	def __init__(self, playerId:int, playerName:str, breed:int, sex:bool, level:int):
		self.playerId=playerId
		self.playerName=playerName
		self.breed=breed
		self.sex=sex
		self.level=level