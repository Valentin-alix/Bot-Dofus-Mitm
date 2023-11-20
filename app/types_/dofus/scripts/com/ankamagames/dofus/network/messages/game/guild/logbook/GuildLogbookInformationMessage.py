from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.guild.logbook.GuildLogbookEntryBasicInformation import GuildLogbookEntryBasicInformation
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.guild.logbook.GuildLogbookEntryBasicInformation import GuildLogbookEntryBasicInformation
class GuildLogbookInformationMessage:
	def __init__(self, globalActivities:list[GuildLogbookEntryBasicInformation], chestActivities:list[GuildLogbookEntryBasicInformation]):
		self.globalActivities=globalActivities
		self.chestActivities=chestActivities