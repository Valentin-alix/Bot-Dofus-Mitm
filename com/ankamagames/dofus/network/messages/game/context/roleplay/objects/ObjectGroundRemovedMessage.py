from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ObjectGroundRemovedMessage(NetworkMessage):
    cell:int
    

    def init(self, cell_:int):
        self.cell = cell_
        
        super().__init__()
    
    