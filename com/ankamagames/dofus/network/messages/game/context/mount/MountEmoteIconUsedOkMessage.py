from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MountEmoteIconUsedOkMessage(NetworkMessage):
    mountId:int
    reactionType:int
    

    def init(self, mountId_:int, reactionType_:int):
        self.mountId = mountId_
        self.reactionType = reactionType_
        
        super().__init__()
    
    