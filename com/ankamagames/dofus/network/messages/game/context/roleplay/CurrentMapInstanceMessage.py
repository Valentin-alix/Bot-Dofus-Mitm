from com.ankamagames.dofus.network.messages.game.context.roleplay.CurrentMapMessage import CurrentMapMessage


class CurrentMapInstanceMessage(CurrentMapMessage):
    instantiatedMapId:int
    

    def init(self, instantiatedMapId_:int, mapId_:int):
        self.instantiatedMapId = instantiatedMapId_
        
        super().__init__(mapId_)
    
    