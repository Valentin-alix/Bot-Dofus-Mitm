from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayDelayedActionMessage(NetworkMessage):
    delayedCharacterId:int
    delayTypeId:int
    delayEndTime:int
    

    def init(self, delayedCharacterId_:int, delayTypeId_:int, delayEndTime_:int):
        self.delayedCharacterId = delayedCharacterId_
        self.delayTypeId = delayTypeId_
        self.delayEndTime = delayEndTime_
        
        super().__init__()
    
    