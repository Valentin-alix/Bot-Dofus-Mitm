from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class IdolSelectErrorMessage(NetworkMessage):
    reason:int
    idolId:int
    activate:bool
    party:bool
    activate:bool
    party:bool
    

    def init(self, reason_:int, idolId_:int, activate_:bool, party_:bool):
        self.reason = reason_
        self.idolId = idolId_
        self.activate = activate_
        self.party = party_
        
        super().__init__()
    
    