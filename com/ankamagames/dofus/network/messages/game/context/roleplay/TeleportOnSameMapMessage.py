from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TeleportOnSameMapMessage(NetworkMessage):
    targetId:int
    cellId:int
    

    def init(self, targetId_:int, cellId_:int):
        self.targetId = targetId_
        self.cellId = cellId_
        
        super().__init__()
    
    