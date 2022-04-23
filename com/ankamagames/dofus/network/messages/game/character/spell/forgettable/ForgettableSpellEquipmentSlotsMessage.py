from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ForgettableSpellEquipmentSlotsMessage(NetworkMessage):
    quantity:int
    

    def init(self, quantity_:int):
        self.quantity = quantity_
        
        super().__init__()
    
    