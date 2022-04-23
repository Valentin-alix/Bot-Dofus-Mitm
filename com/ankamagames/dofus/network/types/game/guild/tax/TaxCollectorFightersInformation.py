from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations
    from com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations
    


class TaxCollectorFightersInformation(NetworkMessage):
    collectorId:int
    allyCharactersInformations:list['CharacterMinimalPlusLookInformations']
    enemyCharactersInformations:list['CharacterMinimalPlusLookInformations']
    

    def init(self, collectorId_:int, allyCharactersInformations_:list['CharacterMinimalPlusLookInformations'], enemyCharactersInformations_:list['CharacterMinimalPlusLookInformations']):
        self.collectorId = collectorId_
        self.allyCharactersInformations = allyCharactersInformations_
        self.enemyCharactersInformations = enemyCharactersInformations_
        
        super().__init__()
    
    