from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightEffectTriggerCount(NetworkMessage):
    effectId:int
    targetId:int
    count:int
    

    def init(self, effectId_:int, targetId_:int, count_:int):
        self.effectId = effectId_
        self.targetId = targetId_
        self.count = count_
        
        super().__init__()
    
    