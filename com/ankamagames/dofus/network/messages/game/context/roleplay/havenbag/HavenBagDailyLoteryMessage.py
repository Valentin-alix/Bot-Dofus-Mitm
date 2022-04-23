from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HavenBagDailyLoteryMessage(NetworkMessage):
    returnType:int
    gameActionId:str
    

    def init(self, returnType_:int, gameActionId_:str):
        self.returnType = returnType_
        self.gameActionId = gameActionId_
        
        super().__init__()
    
    