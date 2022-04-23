from com.ankamagames.dofus.network.types.game.data.items.Item import Item


class ObjectItemQuantity(Item):
    objectUID:int
    quantity:int
    

    def init(self, objectUID_:int, quantity_:int):
        self.objectUID = objectUID_
        self.quantity = quantity_
        
        super().__init__()
    
    