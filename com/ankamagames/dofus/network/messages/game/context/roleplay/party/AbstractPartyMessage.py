from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AbstractPartyMessage(NetworkMessage):
    partyId:int
    

    def init(self, partyId_:int):
        self.partyId = partyId_
        
        super().__init__()
    
    