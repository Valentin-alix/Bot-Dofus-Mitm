from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterNamedInformations import GameFightFighterNamedInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.alignment.ActorAlignmentInformations import ActorAlignmentInformations
    from com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus
    from com.ankamagames.dofus.network.types.game.context.fight.GameContextBasicSpawnInformation import GameContextBasicSpawnInformation
    from com.ankamagames.dofus.network.types.game.context.fight.GameFightCharacteristics import GameFightCharacteristics
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    from com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations
    


class GameFightCharacterInformations(GameFightFighterNamedInformations):
    level:int
    alignmentInfos:'ActorAlignmentInformations'
    breed:int
    sex:bool
    

    def init(self, level_:int, alignmentInfos_:'ActorAlignmentInformations', breed_:int, sex_:bool, name_:str, status_:'PlayerStatus', leagueId_:int, ladderPosition_:int, hiddenInPrefight_:bool, spawnInfo_:'GameContextBasicSpawnInformation', wave_:int, stats_:'GameFightCharacteristics', previousPositions_:list[int], look_:'EntityLook', contextualId_:int, disposition_:'EntityDispositionInformations'):
        self.level = level_
        self.alignmentInfos = alignmentInfos_
        self.breed = breed_
        self.sex = sex_
        
        super().__init__(name_, status_, leagueId_, ladderPosition_, hiddenInPrefight_, spawnInfo_, wave_, stats_, previousPositions_, look_, contextualId_, disposition_)
    
    