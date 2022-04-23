from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayPlayerFightRequestMessage(NetworkMessage):
    targetId:int
    targetCellId:int
    friendly:bool
    

    def init(self, targetId_:int, targetCellId_:int, friendly_:bool):
        self.targetId = targetId_
        self.targetCellId = targetCellId_
        self.friendly = friendly_
        
        super().__init__()
    
    