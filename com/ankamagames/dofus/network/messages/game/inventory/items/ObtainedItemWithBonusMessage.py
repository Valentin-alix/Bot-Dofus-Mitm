from com.ankamagames.dofus.network.messages.game.inventory.items.ObtainedItemMessage import ObtainedItemMessage


class ObtainedItemWithBonusMessage(ObtainedItemMessage):
    bonusQuantity:int
    

    def init(self, bonusQuantity_:int, genericId_:int, baseQuantity_:int):
        self.bonusQuantity = bonusQuantity_
        
        super().__init__(genericId_, baseQuantity_)
    
    