from com.ankamagames.dofus.network.messages.game.inventory.items.ObjectErrorMessage import ObjectErrorMessage


class SymbioticObjectErrorMessage(ObjectErrorMessage):
    errorCode:int
    

    def init(self, errorCode_:int, reason_:int):
        self.errorCode = errorCode_
        
        super().__init__(reason_)
    
    