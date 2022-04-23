from com.ankamagames.dofus.network.types.game.guild.logbook.GuildLogbookEntryBasicInformation import GuildLogbookEntryBasicInformation
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.MapCoordinatesExtended import MapCoordinatesExtended
    


class GuildPaddockActivity(GuildLogbookEntryBasicInformation):
    playerId:int
    playerName:str
    paddockCoordinates:'MapCoordinatesExtended'
    farmId:int
    paddockEventType:int
    

    def init(self, playerId_:int, playerName_:str, paddockCoordinates_:'MapCoordinatesExtended', farmId_:int, paddockEventType_:int, id_:int, date_:int):
        self.playerId = playerId_
        self.playerName = playerName_
        self.paddockCoordinates = paddockCoordinates_
        self.farmId = farmId_
        self.paddockEventType = paddockEventType_
        
        super().__init__(id_, date_)
    
    