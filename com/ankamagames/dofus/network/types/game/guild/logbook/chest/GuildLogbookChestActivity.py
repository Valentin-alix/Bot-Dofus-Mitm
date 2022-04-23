from com.ankamagames.dofus.network.types.game.guild.logbook.GuildLogbookEntryBasicInformation import GuildLogbookEntryBasicInformation
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.ObjectItemNotInContainer import ObjectItemNotInContainer
    


class GuildLogbookChestActivity(GuildLogbookEntryBasicInformation):
    playerId:int
    playerName:str
    eventType:int
    quantity:int
    object:'ObjectItemNotInContainer'
    

    def init(self, playerId_:int, playerName_:str, eventType_:int, quantity_:int, object_:'ObjectItemNotInContainer', id_:int, date_:int):
        self.playerId = playerId_
        self.playerName = playerName_
        self.eventType = eventType_
        self.quantity = quantity_
        self.object = object_
        
        super().__init__(id_, date_)
    
    