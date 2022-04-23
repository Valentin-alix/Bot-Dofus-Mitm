from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayDelayedActionFinishedMessage(NetworkMessage):
    delayedCharacterId:int
    delayTypeId:int
    

    def init(self, delayedCharacterId_:int, delayTypeId_:int):
        self.delayedCharacterId = delayedCharacterId_
        self.delayTypeId = delayTypeId_
        
        super().__init__()
    
    