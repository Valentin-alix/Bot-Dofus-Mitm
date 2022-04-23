from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class BreachReward(NetworkMessage):
    id:int
    buyLocks:list[int]
    buyCriterion:str
    remainingQty:int
    price:int
    

    def init(self, id_:int, buyLocks_:list[int], buyCriterion_:str, remainingQty_:int, price_:int):
        self.id = id_
        self.buyLocks = buyLocks_
        self.buyCriterion = buyCriterion_
        self.remainingQty = remainingQty_
        self.price = price_
        
        super().__init__()
    
    