from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MoodSmileyUpdateMessage(NetworkMessage):
    accountId:int
    playerId:int
    smileyId:int
    

    def init(self, accountId_:int, playerId_:int, smileyId_:int):
        self.accountId = accountId_
        self.playerId = playerId_
        self.smileyId = smileyId_
        
        super().__init__()
    
    