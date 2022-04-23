from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ItemForPreset(NetworkMessage):
    position:int
    objGid:int
    objUid:int
    

    def init(self, position_:int, objGid_:int, objUid_:int):
        self.position = position_
        self.objGid = objGid_
        self.objUid = objUid_
        
        super().__init__()
    
    