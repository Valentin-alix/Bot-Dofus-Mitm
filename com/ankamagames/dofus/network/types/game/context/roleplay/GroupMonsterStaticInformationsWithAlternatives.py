from com.ankamagames.dofus.network.types.game.context.roleplay.GroupMonsterStaticInformations import GroupMonsterStaticInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.AlternativeMonstersInGroupLightInformations import AlternativeMonstersInGroupLightInformations
    from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterInGroupLightInformations import MonsterInGroupLightInformations
    from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterInGroupInformations import MonsterInGroupInformations
    


class GroupMonsterStaticInformationsWithAlternatives(GroupMonsterStaticInformations):
    alternatives:list['AlternativeMonstersInGroupLightInformations']
    

    def init(self, alternatives_:list['AlternativeMonstersInGroupLightInformations'], mainCreatureLightInfos_:'MonsterInGroupLightInformations', underlings_:list['MonsterInGroupInformations']):
        self.alternatives = alternatives_
        
        super().__init__(mainCreatureLightInfos_, underlings_)
    
    