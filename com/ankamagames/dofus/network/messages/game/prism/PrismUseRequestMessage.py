from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PrismUseRequestMessage(NetworkMessage):
    moduleToUse:int
    

    def init(self, moduleToUse_:int):
        self.moduleToUse = moduleToUse_
        
        super().__init__()
    
    