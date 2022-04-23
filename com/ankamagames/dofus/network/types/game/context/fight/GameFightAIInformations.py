from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterInformations import GameFightFighterInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.fight.GameContextBasicSpawnInformation import GameContextBasicSpawnInformation
    from com.ankamagames.dofus.network.types.game.context.fight.GameFightCharacteristics import GameFightCharacteristics
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    from com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations
    


class GameFightAIInformations(GameFightFighterInformations):
    

    def init(self, spawnInfo_:'GameContextBasicSpawnInformation', wave_:int, stats_:'GameFightCharacteristics', previousPositions_:list[int], look_:'EntityLook', contextualId_:int, disposition_:'EntityDispositionInformations'):
        
        super().__init__(spawnInfo_, wave_, stats_, previousPositions_, look_, contextualId_, disposition_)
    
    