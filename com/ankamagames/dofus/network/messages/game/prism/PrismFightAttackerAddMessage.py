from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations
    


class PrismFightAttackerAddMessage(NetworkMessage):
    subAreaId:int
    fightId:int
    attacker:'CharacterMinimalPlusLookInformations'
    

    def init(self, subAreaId_:int, fightId_:int, attacker_:'CharacterMinimalPlusLookInformations'):
        self.subAreaId = subAreaId_
        self.fightId = fightId_
        self.attacker = attacker_
        
        super().__init__()
    
    