from com.ankamagames.dofus.network.messages.game.inventory.items.ObjectUseMessage import ObjectUseMessage


class ObjectUseMultipleMessage(ObjectUseMessage):
    quantity:int
    

    def init(self, quantity_:int, objectUID_:int):
        self.quantity = quantity_
        
        super().__init__(objectUID_)
    
    