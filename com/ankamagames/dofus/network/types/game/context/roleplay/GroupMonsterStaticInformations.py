from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterInGroupLightInformations import MonsterInGroupLightInformations
    from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterInGroupInformations import MonsterInGroupInformations
    


class GroupMonsterStaticInformations(NetworkMessage):
    mainCreatureLightInfos:'MonsterInGroupLightInformations'
    underlings:list['MonsterInGroupInformations']
    

    def init(self, mainCreatureLightInfos_:'MonsterInGroupLightInformations', underlings_:list['MonsterInGroupInformations']):
        self.mainCreatureLightInfos = mainCreatureLightInfos_
        self.underlings = underlings_
        
        super().__init__()
    
    