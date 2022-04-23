from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.choice.CharacterBaseInformations import CharacterBaseInformations
    


class CharacterSelectedSuccessMessage(NetworkMessage):
    infos:'CharacterBaseInformations'
    isCollectingStats:bool
    

    def init(self, infos_:'CharacterBaseInformations', isCollectingStats_:bool):
        self.infos = infos_
        self.isCollectingStats = isCollectingStats_
        
        super().__init__()
    
    