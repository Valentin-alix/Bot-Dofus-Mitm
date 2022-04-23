from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class DecraftedItemStackInfo(NetworkMessage):
    objectUID:int
    bonusMin:int
    bonusMax:int
    runesId:list[int]
    runesQty:list[int]
    

    def init(self, objectUID_:int, bonusMin_:int, bonusMax_:int, runesId_:list[int], runesQty_:list[int]):
        self.objectUID = objectUID_
        self.bonusMin = bonusMin_
        self.bonusMax = bonusMax_
        self.runesId = runesId_
        self.runesQty = runesQty_
        
        super().__init__()
    
    