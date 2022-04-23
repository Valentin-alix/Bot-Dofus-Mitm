from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class RecycleResultMessage(NetworkMessage):
    nuggetsForPrism:int
    nuggetsForPlayer:int
    

    def init(self, nuggetsForPrism_:int, nuggetsForPlayer_:int):
        self.nuggetsForPrism = nuggetsForPrism_
        self.nuggetsForPlayer = nuggetsForPlayer_
        
        super().__init__()
    
    