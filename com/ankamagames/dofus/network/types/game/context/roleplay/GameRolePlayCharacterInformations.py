from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayHumanoidInformations import GameRolePlayHumanoidInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.alignment.ActorAlignmentInformations import ActorAlignmentInformations
    from com.ankamagames.dofus.network.types.game.context.roleplay.HumanInformations import HumanInformations
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    from com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations
    


class GameRolePlayCharacterInformations(GameRolePlayHumanoidInformations):
    alignmentInfos:'ActorAlignmentInformations'
    

    def init(self, alignmentInfos_:'ActorAlignmentInformations', humanoidInfo_:'HumanInformations', accountId_:int, name_:str, look_:'EntityLook', contextualId_:int, disposition_:'EntityDispositionInformations'):
        self.alignmentInfos = alignmentInfos_
        
        super().__init__(humanoidInfo_, accountId_, name_, look_, contextualId_, disposition_)
    
    