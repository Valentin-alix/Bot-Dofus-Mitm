from com.ankamagames.dofus.network.types.game.context.fight.GameFightAIInformations import GameFightAIInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.fight.GameContextBasicSpawnInformation import GameContextBasicSpawnInformation
    from com.ankamagames.dofus.network.types.game.context.fight.GameFightCharacteristics import GameFightCharacteristics
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    from com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations
    


class GameFightMonsterInformations(GameFightAIInformations):
    creatureGenericId:int
    creatureGrade:int
    creatureLevel:int
    

    def init(self, creatureGenericId_:int, creatureGrade_:int, creatureLevel_:int, spawnInfo_:'GameContextBasicSpawnInformation', wave_:int, stats_:'GameFightCharacteristics', previousPositions_:list[int], look_:'EntityLook', contextualId_:int, disposition_:'EntityDispositionInformations'):
        self.creatureGenericId = creatureGenericId_
        self.creatureGrade = creatureGrade_
        self.creatureLevel = creatureLevel_
        
        super().__init__(spawnInfo_, wave_, stats_, previousPositions_, look_, contextualId_, disposition_)
    
    