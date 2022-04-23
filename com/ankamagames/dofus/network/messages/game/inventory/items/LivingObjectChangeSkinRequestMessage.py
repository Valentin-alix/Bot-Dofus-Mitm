from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class LivingObjectChangeSkinRequestMessage(NetworkMessage):
    livingUID:int
    livingPosition:int
    skinId:int
    

    def init(self, livingUID_:int, livingPosition_:int, skinId_:int):
        self.livingUID = livingUID_
        self.livingPosition = livingPosition_
        self.skinId = skinId_
        
        super().__init__()
    
    