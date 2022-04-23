from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MountRenamedMessage(NetworkMessage):
    mountId:int
    name:str
    

    def init(self, mountId_:int, name_:str):
        self.mountId = mountId_
        self.name = name_
        
        super().__init__()
    
    