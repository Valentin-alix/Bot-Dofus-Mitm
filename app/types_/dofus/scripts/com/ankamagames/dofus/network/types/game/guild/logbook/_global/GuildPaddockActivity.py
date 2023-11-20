from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.guild.logbook.GuildLogbookEntryBasicInformation import GuildLogbookEntryBasicInformation
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.MapCoordinatesExtended import MapCoordinatesExtended
class GuildPaddockActivity(GuildLogbookEntryBasicInformation):
	def __init__(self, playerId:int, playerName:str, paddockCoordinates:MapCoordinatesExtended, farmId:float, paddockEventType:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.playerId=playerId
		self.playerName=playerName
		self.paddockCoordinates=paddockCoordinates
		self.farmId=farmId
		self.paddockEventType=paddockEventType