from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.guild.logbook.GuildLogbookEntryBasicInformation import GuildLogbookEntryBasicInformation
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.rank.RankMinimalInformation import RankMinimalInformation
class GuildPlayerRankUpdateActivity(GuildLogbookEntryBasicInformation):
	def __init__(self, guildRankMinimalInfos:RankMinimalInformation, sourcePlayerId:int, targetPlayerId:int, sourcePlayerName:str, targetPlayerName:str, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.guildRankMinimalInfos=guildRankMinimalInfos
		self.sourcePlayerId=sourcePlayerId
		self.targetPlayerId=targetPlayerId
		self.sourcePlayerName=sourcePlayerName
		self.targetPlayerName=targetPlayerName