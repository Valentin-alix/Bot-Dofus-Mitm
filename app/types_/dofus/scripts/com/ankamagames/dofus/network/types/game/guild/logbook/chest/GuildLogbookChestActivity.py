from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.guild.logbook.GuildLogbookEntryBasicInformation import GuildLogbookEntryBasicInformation
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.ObjectItemNotInContainer import ObjectItemNotInContainer
class GuildLogbookChestActivity(GuildLogbookEntryBasicInformation):
	def __init__(self, playerId:int, playerName:str, eventType:int, quantity:int, object:ObjectItemNotInContainer, sourceTabId:int, destinationTabId:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.playerId=playerId
		self.playerName=playerName
		self.eventType=eventType
		self.quantity=quantity
		self.object=object
		self.sourceTabId=sourceTabId
		self.destinationTabId=destinationTabId