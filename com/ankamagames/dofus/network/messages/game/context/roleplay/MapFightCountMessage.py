from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MapFightCountMessage(NetworkMessage):
    fightCount:int
    

    def init(self, fightCount_:int):
        self.fightCount = fightCount_
        
        super().__init__()
    
    