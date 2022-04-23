from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ChatSmileyMessage(NetworkMessage):
    entityId:int
    smileyId:int
    accountId:int
    

    def init(self, entityId_:int, smileyId_:int, accountId_:int):
        self.entityId = entityId_
        self.smileyId = smileyId_
        self.accountId = accountId_
        
        super().__init__()
    
    