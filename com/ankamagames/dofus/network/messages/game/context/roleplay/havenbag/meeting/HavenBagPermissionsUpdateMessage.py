from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HavenBagPermissionsUpdateMessage(NetworkMessage):
    permissions:int
    

    def init(self, permissions_:int):
        self.permissions = permissions_
        
        super().__init__()
    
    