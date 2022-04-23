from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayNpcInformations import GameRolePlayNpcInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.quest.GameRolePlayNpcQuestFlag import GameRolePlayNpcQuestFlag
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    from com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations
    


class GameRolePlayNpcWithQuestInformations(GameRolePlayNpcInformations):
    questFlag:'GameRolePlayNpcQuestFlag'
    

    def init(self, questFlag_:'GameRolePlayNpcQuestFlag', npcId_:int, sex_:bool, specialArtworkId_:int, look_:'EntityLook', contextualId_:int, disposition_:'EntityDispositionInformations'):
        self.questFlag = questFlag_
        
        super().__init__(npcId_, sex_, specialArtworkId_, look_, contextualId_, disposition_)
    
    