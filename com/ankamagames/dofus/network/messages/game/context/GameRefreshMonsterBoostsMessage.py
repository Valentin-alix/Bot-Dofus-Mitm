from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterBoosts import MonsterBoosts
    from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterBoosts import MonsterBoosts
    


class GameRefreshMonsterBoostsMessage(NetworkMessage):
    monsterBoosts:list['MonsterBoosts']
    familyBoosts:list['MonsterBoosts']
    

    def init(self, monsterBoosts_:list['MonsterBoosts'], familyBoosts_:list['MonsterBoosts']):
        self.monsterBoosts = monsterBoosts_
        self.familyBoosts = familyBoosts_
        
        super().__init__()
    
    