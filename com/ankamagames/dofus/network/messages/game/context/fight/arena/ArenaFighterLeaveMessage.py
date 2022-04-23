from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.CharacterBasicMinimalInformations import CharacterBasicMinimalInformations
    


class ArenaFighterLeaveMessage(NetworkMessage):
    leaver:'CharacterBasicMinimalInformations'
    

    def init(self, leaver_:'CharacterBasicMinimalInformations'):
        self.leaver = leaver_
        
        super().__init__()
    
    