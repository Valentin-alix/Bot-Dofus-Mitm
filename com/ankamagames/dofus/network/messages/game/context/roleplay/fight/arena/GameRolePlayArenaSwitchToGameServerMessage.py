from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayArenaSwitchToGameServerMessage(NetworkMessage):
    validToken:bool
    ticket:list[int]
    homeServerId:int
    

    def init(self, validToken_:bool, ticket_:list[int], homeServerId_:int):
        self.validToken = validToken_
        self.ticket = ticket_
        self.homeServerId = homeServerId_
        
        super().__init__()
    
    