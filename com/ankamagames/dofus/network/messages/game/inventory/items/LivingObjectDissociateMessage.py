from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class LivingObjectDissociateMessage(NetworkMessage):
    livingUID:int
    livingPosition:int
    

    def init(self, livingUID_:int, livingPosition_:int):
        self.livingUID = livingUID_
        self.livingPosition = livingPosition_
        
        super().__init__()
    
    