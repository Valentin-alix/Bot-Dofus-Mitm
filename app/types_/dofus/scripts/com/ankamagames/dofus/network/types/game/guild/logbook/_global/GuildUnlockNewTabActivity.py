from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.guild.logbook.GuildLogbookEntryBasicInformation import GuildLogbookEntryBasicInformation
if TYPE_CHECKING:
	...
class GuildUnlockNewTabActivity(GuildLogbookEntryBasicInformation):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		...