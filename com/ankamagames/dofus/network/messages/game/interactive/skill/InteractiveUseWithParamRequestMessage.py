from com.ankamagames.dofus.network.messages.game.interactive.InteractiveUseRequestMessage import InteractiveUseRequestMessage


class InteractiveUseWithParamRequestMessage(InteractiveUseRequestMessage):
    id:int
    

    def init(self, id_:int, elemId_:int, skillInstanceUid_:int):
        self.id = id_
        
        super().__init__(elemId_, skillInstanceUid_)
    
    