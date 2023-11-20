from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.guild.logbook.GuildLogbookEntryBasicInformation import GuildLogbookEntryBasicInformation
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.rank.RankMinimalInformation import RankMinimalInformation
class GuildRankActivity(GuildLogbookEntryBasicInformation):
	def __init__(self, rankActivityType:int, guildRankMinimalInfos:RankMinimalInformation, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.rankActivityType=rankActivityType
		self.guildRankMinimalInfos=guildRankMinimalInfos