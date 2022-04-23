from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MonsterBoosts(NetworkMessage):
    id:int
    xpBoost:int
    dropBoost:int
    

    def init(self, id_:int, xpBoost_:int, dropBoost_:int):
        self.id = id_
        self.xpBoost = xpBoost_
        self.dropBoost = dropBoost_
        
        super().__init__()
    
    