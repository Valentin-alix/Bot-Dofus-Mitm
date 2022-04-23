from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PaddockMoveItemRequestMessage(NetworkMessage):
    oldCellId:int
    newCellId:int
    

    def init(self, oldCellId_:int, newCellId_:int):
        self.oldCellId = oldCellId_
        self.newCellId = newCellId_
        
        super().__init__()
    
    