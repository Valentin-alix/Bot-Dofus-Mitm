from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.friend.AbstractContactInformations import AbstractContactInformations
if TYPE_CHECKING:
	...
class LeagueFriendInformations(AbstractContactInformations):
	def __init__(self, playerId:int, playerName:str, breed:int, sex:bool, level:int, leagueId:int, totalLeaguePoints:int, ladderPosition:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.playerId=playerId
		self.playerName=playerName
		self.breed=breed
		self.sex=sex
		self.level=level
		self.leagueId=leagueId
		self.totalLeaguePoints=totalLeaguePoints
		self.ladderPosition=ladderPosition