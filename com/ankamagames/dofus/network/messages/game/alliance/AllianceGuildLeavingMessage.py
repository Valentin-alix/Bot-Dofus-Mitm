from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AllianceGuildLeavingMessage(NetworkMessage):
    kicked:bool
    guildId:int
    

    def init(self, kicked_:bool, guildId_:int):
        self.kicked = kicked_
        self.guildId = guildId_
        
        super().__init__()
    
    