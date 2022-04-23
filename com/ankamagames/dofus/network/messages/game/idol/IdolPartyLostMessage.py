from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class IdolPartyLostMessage(NetworkMessage):
    idolId:int
    

    def init(self, idolId_:int):
        self.idolId = idolId_
        
        super().__init__()
    
    