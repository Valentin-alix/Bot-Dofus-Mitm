from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ArenaLeagueRanking:
	def __init__(self, rank:int, leagueId:int, leaguePoints:int, totalLeaguePoints:int, ladderPosition:int):
		self.rank=rank
		self.leagueId=leagueId
		self.leaguePoints=leaguePoints
		self.totalLeaguePoints=totalLeaguePoints
		self.ladderPosition=ladderPosition