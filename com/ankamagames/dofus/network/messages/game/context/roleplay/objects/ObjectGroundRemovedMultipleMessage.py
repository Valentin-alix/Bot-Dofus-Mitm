from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ObjectGroundRemovedMultipleMessage(NetworkMessage):
    cells:list[int]
    

    def init(self, cells_:list[int]):
        self.cells = cells_
        
        super().__init__()
    
    