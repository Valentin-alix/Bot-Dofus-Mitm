from com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations


class IdentifiedEntityDispositionInformations(EntityDispositionInformations):
    id:int
    

    def init(self, id_:int, cellId_:int, direction_:int):
        self.id = id_
        
        super().__init__(cellId_, direction_)
    
    