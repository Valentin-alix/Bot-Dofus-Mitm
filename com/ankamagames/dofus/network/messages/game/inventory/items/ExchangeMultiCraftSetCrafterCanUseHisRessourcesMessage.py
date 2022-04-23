from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeMultiCraftSetCrafterCanUseHisRessourcesMessage(NetworkMessage):
    allow:bool
    

    def init(self, allow_:bool):
        self.allow = allow_
        
        super().__init__()
    
    