from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class DebugHighlightCellsMessage(NetworkMessage):
    color:int
    cells:list[int]
    

    def init(self, color_:int, cells_:list[int]):
        self.color = color_
        self.cells = cells_
        
        super().__init__()
    
    