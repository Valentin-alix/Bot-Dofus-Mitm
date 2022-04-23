from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MountRenameRequestMessage(NetworkMessage):
    name:str
    mountId:int
    

    def init(self, name_:str, mountId_:int):
        self.name = name_
        self.mountId = mountId_
        
        super().__init__()
    
    