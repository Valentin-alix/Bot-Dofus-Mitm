from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PortalUseRequestMessage(NetworkMessage):
    portalId:int
    

    def init(self, portalId_:int):
        self.portalId = portalId_
        
        super().__init__()
    
    