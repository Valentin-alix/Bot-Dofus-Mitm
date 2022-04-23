from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayGroupMonsterInformations import GameRolePlayGroupMonsterInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.GroupMonsterStaticInformations import GroupMonsterStaticInformations
    from com.ankamagames.dofus.network.types.game.context.roleplay.GroupMonsterStaticInformations import GroupMonsterStaticInformations
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    from com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations
    


class GameRolePlayGroupMonsterWaveInformations(GameRolePlayGroupMonsterInformations):
    nbWaves:int
    alternatives:list['GroupMonsterStaticInformations']
    

    def init(self, nbWaves_:int, alternatives_:list['GroupMonsterStaticInformations'], staticInfos_:'GroupMonsterStaticInformations', lootShare_:int, alignmentSide_:int, keyRingBonus_:bool, hasHardcoreDrop_:bool, hasAVARewardToken_:bool, look_:'EntityLook', contextualId_:int, disposition_:'EntityDispositionInformations'):
        self.nbWaves = nbWaves_
        self.alternatives = alternatives_
        
        super().__init__(staticInfos_, lootShare_, alignmentSide_, keyRingBonus_, hasHardcoreDrop_, hasAVARewardToken_, look_, contextualId_, disposition_)
    
    