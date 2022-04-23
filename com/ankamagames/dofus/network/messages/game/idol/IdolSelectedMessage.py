from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class IdolSelectedMessage(NetworkMessage):
    idolId:int
    activate:bool
    party:bool
    activate:bool
    party:bool
    

    def init(self, idolId_:int, activate_:bool, party_:bool):
        self.idolId = idolId_
        self.activate = activate_
        self.party = party_
        
        super().__init__()
    
    