from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class FriendDeleteRequestMessage(NetworkMessage):
    accountId:int
    

    def init(self, accountId_:int):
        self.accountId = accountId_
        
        super().__init__()
    
    