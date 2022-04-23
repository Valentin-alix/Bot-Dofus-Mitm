from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ObjectGroundListAddedMessage(NetworkMessage):
    cells:list[int]
    referenceIds:list[int]
    

    def init(self, cells_:list[int], referenceIds_:list[int]):
        self.cells = cells_
        self.referenceIds = referenceIds_
        
        super().__init__()
    
    