from com.ankamagames.dofus.network.types.game.data.items.Item import Item


class ObjectItemGenericQuantity(Item):
    objectGID:int
    quantity:int
    

    def init(self, objectGID_:int, quantity_:int):
        self.objectGID = objectGID_
        self.quantity = quantity_
        
        super().__init__()
    
    