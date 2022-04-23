from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect
    


class ObjectEffects(NetworkMessage):
    effects:list['ObjectEffect']
    

    def init(self, effects_:list['ObjectEffect']):
        self.effects = effects_
        
        super().__init__()
    
    