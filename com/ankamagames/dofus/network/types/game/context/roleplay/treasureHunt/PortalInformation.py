from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PortalInformation(NetworkMessage):
    portalId:int
    areaId:int
    

    def init(self, portalId_:int, areaId_:int):
        self.portalId = portalId_
        self.areaId = areaId_
        
        super().__init__()
    
    