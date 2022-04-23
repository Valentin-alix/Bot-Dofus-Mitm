from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameActionFightCastOnTargetRequestMessage(NetworkMessage):
    spellId:int
    targetId:int
    

    def init(self, spellId_:int, targetId_:int):
        self.spellId = spellId_
        self.targetId = targetId_
        
        super().__init__()
    
    