from com.ankamagames.dofus.network.types.game.context.GameContextActorPositionInformations import GameContextActorPositionInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    from com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations
    


class GameContextActorInformations(GameContextActorPositionInformations):
    look:'EntityLook'
    

    def init(self, look_:'EntityLook', contextualId_:int, disposition_:'EntityDispositionInformations'):
        self.look = look_
        
        super().__init__(contextualId_, disposition_)
    
    