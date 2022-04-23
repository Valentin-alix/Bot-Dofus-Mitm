from com.ankamagames.dofus.network.types.game.context.fight.GameFightMonsterInformations import GameFightMonsterInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.alignment.ActorAlignmentInformations import ActorAlignmentInformations
    from com.ankamagames.dofus.network.types.game.context.fight.GameContextBasicSpawnInformation import GameContextBasicSpawnInformation
    from com.ankamagames.dofus.network.types.game.context.fight.GameFightCharacteristics import GameFightCharacteristics
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    from com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations
    


class GameFightMonsterWithAlignmentInformations(GameFightMonsterInformations):
    alignmentInfos:'ActorAlignmentInformations'
    

    def init(self, alignmentInfos_:'ActorAlignmentInformations', creatureGenericId_:int, creatureGrade_:int, creatureLevel_:int, spawnInfo_:'GameContextBasicSpawnInformation', wave_:int, stats_:'GameFightCharacteristics', previousPositions_:list[int], look_:'EntityLook', contextualId_:int, disposition_:'EntityDispositionInformations'):
        self.alignmentInfos = alignmentInfos_
        
        super().__init__(creatureGenericId_, creatureGrade_, creatureLevel_, spawnInfo_, wave_, stats_, previousPositions_, look_, contextualId_, disposition_)
    
    