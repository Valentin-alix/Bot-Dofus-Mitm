from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeMultiCraftCrafterCanUseHisRessourcesMessage(NetworkMessage):
    allowed:bool
    

    def init(self, allowed_:bool):
        self.allowed = allowed_
        
        super().__init__()
    
    