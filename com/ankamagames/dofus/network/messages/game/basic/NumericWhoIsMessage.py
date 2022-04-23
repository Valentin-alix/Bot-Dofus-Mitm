from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class NumericWhoIsMessage(NetworkMessage):
    playerId:int
    accountId:int
    

    def init(self, playerId_:int, accountId_:int):
        self.playerId = playerId_
        self.accountId = accountId_
        
        super().__init__()
    
    