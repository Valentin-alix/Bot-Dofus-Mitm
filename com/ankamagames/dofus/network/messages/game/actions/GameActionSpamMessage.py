from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameActionSpamMessage(NetworkMessage):
    cells:list[int]
    

    def init(self, cells_:list[int]):
        self.cells = cells_
        
        super().__init__()
    
    