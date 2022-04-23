from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildFightLeaveRequestMessage(NetworkMessage):
    taxCollectorId:int
    characterId:int
    

    def init(self, taxCollectorId_:int, characterId_:int):
        self.taxCollectorId = taxCollectorId_
        self.characterId = characterId_
        
        super().__init__()
    
    