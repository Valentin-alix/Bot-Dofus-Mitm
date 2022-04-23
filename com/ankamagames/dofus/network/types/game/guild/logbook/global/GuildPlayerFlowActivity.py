from com.ankamagames.dofus.network.types.game.guild.logbook.GuildLogbookEntryBasicInformation import GuildLogbookEntryBasicInformation


class GuildPlayerFlowActivity(GuildLogbookEntryBasicInformation):
    playerId:int
    playerName:str
    playerFlowEventType:int
    

    def init(self, playerId_:int, playerName_:str, playerFlowEventType_:int, id_:int, date_:int):
        self.playerId = playerId_
        self.playerName = playerName_
        self.playerFlowEventType = playerFlowEventType_
        
        super().__init__(id_, date_)
    
    