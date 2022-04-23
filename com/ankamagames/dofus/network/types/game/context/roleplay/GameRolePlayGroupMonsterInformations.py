from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayActorInformations import GameRolePlayActorInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.GroupMonsterStaticInformations import GroupMonsterStaticInformations
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    from com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations
    


class GameRolePlayGroupMonsterInformations(GameRolePlayActorInformations):
    staticInfos:'GroupMonsterStaticInformations'
    lootShare:int
    alignmentSide:int
    keyRingBonus:bool
    hasHardcoreDrop:bool
    hasAVARewardToken:bool
    keyRingBonus:bool
    hasHardcoreDrop:bool
    hasAVARewardToken:bool
    

    def init(self, staticInfos_:'GroupMonsterStaticInformations', lootShare_:int, alignmentSide_:int, keyRingBonus_:bool, hasHardcoreDrop_:bool, hasAVARewardToken_:bool, look_:'EntityLook', contextualId_:int, disposition_:'EntityDispositionInformations'):
        self.staticInfos = staticInfos_
        self.lootShare = lootShare_
        self.alignmentSide = alignmentSide_
        self.keyRingBonus = keyRingBonus_
        self.hasHardcoreDrop = hasHardcoreDrop_
        self.hasAVARewardToken = hasAVARewardToken_
        
        super().__init__(look_, contextualId_, disposition_)
    
    