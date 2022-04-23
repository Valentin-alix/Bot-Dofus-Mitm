from com.ankamagames.dofus.network.messages.game.context.roleplay.houses.HouseSellRequestMessage import HouseSellRequestMessage


class HouseSellFromInsideRequestMessage(HouseSellRequestMessage):
    

    def init(self, instanceId_:int, amount_:int, forSale_:bool):
        
        super().__init__(instanceId_, amount_, forSale_)
    
    