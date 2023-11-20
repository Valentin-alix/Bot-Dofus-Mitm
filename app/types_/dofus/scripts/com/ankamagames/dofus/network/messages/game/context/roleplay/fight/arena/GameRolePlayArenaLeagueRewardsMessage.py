from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameRolePlayArenaLeagueRewardsMessage:
	def __init__(self, seasonId:int, leagueId:int, ladderPosition:int, endSeasonReward:bool):
		self.seasonId=seasonId
		self.leagueId=leagueId
		self.ladderPosition=ladderPosition
		self.endSeasonReward=endSeasonReward