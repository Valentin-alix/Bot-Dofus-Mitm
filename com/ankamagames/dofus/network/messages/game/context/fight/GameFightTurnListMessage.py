from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightTurnListMessage(NetworkMessage):
    ids:list[int]
    deadsIds:list[int]
    

    def init(self, ids_:list[int], deadsIds_:list[int]):
        self.ids = ids_
        self.deadsIds = deadsIds_
        
        super().__init__()
    
    