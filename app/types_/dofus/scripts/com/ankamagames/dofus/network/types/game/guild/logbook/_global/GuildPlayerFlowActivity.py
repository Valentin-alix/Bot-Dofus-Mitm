from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.guild.logbook.GuildLogbookEntryBasicInformation import GuildLogbookEntryBasicInformation
if TYPE_CHECKING:
	...
class GuildPlayerFlowActivity(GuildLogbookEntryBasicInformation):
	def __init__(self, playerId:int, playerName:str, playerFlowEventType:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.playerId=playerId
		self.playerName=playerName
		self.playerFlowEventType=playerFlowEventType