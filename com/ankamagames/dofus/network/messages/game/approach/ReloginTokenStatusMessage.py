from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ReloginTokenStatusMessage(NetworkMessage):
    validToken:bool
    ticket:list[int]
    

    def init(self, validToken_:bool, ticket_:list[int]):
        self.validToken = validToken_
        self.ticket = ticket_
        
        super().__init__()
    
    