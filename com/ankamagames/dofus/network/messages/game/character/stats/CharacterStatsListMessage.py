from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristicsInformations import CharacterCharacteristicsInformations
    


class CharacterStatsListMessage(NetworkMessage):
    stats:'CharacterCharacteristicsInformations'
    

    def init(self, stats_:'CharacterCharacteristicsInformations'):
        self.stats = stats_
        
        super().__init__()
    
    