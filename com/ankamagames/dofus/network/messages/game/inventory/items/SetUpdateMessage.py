from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect
    


class SetUpdateMessage(NetworkMessage):
    setId:int
    setObjects:list[int]
    setEffects:list['ObjectEffect']
    

    def init(self, setId_:int, setObjects_:list[int], setEffects_:list['ObjectEffect']):
        self.setId = setId_
        self.setObjects = setObjects_
        self.setEffects = setEffects_
        
        super().__init__()
    
    