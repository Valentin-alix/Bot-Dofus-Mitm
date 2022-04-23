from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildVersatileInformations(NetworkMessage):
    guildId:int
    leaderId:int
    guildLevel:int
    nbMembers:int
    

    def init(self, guildId_:int, leaderId_:int, guildLevel_:int, nbMembers_:int):
        self.guildId = guildId_
        self.leaderId = leaderId_
        self.guildLevel = guildLevel_
        self.nbMembers = nbMembers_
        
        super().__init__()
    
    