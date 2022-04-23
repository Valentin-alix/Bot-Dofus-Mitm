from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterInGroupLightInformations import MonsterInGroupLightInformations
    from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterInGroupLightInformations import MonsterInGroupLightInformations
    


class BreachBranch(NetworkMessage):
    room:int
    element:int
    bosses:list['MonsterInGroupLightInformations']
    map:int
    score:int
    relativeScore:int
    monsters:list['MonsterInGroupLightInformations']
    

    def init(self, room_:int, element_:int, bosses_:list['MonsterInGroupLightInformations'], map_:int, score_:int, relativeScore_:int, monsters_:list['MonsterInGroupLightInformations']):
        self.room = room_
        self.element = element_
        self.bosses = bosses_
        self.map = map_
        self.score = score_
        self.relativeScore = relativeScore_
        self.monsters = monsters_
        
        super().__init__()
    
    