from com.ankamagames.dofus.network.messages.game.inventory.items.SymbioticObjectAssociateRequestMessage import SymbioticObjectAssociateRequestMessage


class MimicryObjectFeedAndAssociateRequestMessage(SymbioticObjectAssociateRequestMessage):
    foodUID:int
    foodPos:int
    preview:bool
    

    def init(self, foodUID_:int, foodPos_:int, preview_:bool, symbioteUID_:int, symbiotePos_:int, hostUID_:int, hostPos_:int):
        self.foodUID = foodUID_
        self.foodPos = foodPos_
        self.preview = preview_
        
        super().__init__(symbioteUID_, symbiotePos_, hostUID_, hostPos_)
    
    