from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristics import CharacterCharacteristics
    


class DumpedEntityStatsMessage(NetworkMessage):
    actorId:int
    stats:'CharacterCharacteristics'
    

    def init(self, actorId_:int, stats_:'CharacterCharacteristics'):
        self.actorId = actorId_
        self.stats = stats_
        
        super().__init__()
    
    