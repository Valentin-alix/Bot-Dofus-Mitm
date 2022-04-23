from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class Idol(NetworkMessage):
    id:int
    xpBonusPercent:int
    dropBonusPercent:int
    

    def init(self, id_:int, xpBonusPercent_:int, dropBonusPercent_:int):
        self.id = id_
        self.xpBonusPercent = xpBonusPercent_
        self.dropBonusPercent = dropBonusPercent_
        
        super().__init__()
    
    