from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameDataPlayFarmObjectAnimationMessage(NetworkMessage):
    cellId:list[int]
    

    def init(self, cellId_:list[int]):
        self.cellId = cellId_
        
        super().__init__()
    
    