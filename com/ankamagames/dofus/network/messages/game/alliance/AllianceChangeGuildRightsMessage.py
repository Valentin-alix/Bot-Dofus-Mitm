from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AllianceChangeGuildRightsMessage(NetworkMessage):
    guildId:int
    rights:int
    

    def init(self, guildId_:int, rights_:int):
        self.guildId = guildId_
        self.rights = rights_
        
        super().__init__()
    
    