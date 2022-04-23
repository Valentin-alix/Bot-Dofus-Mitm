from com.ankamagames.dofus.network.messages.game.context.fight.character.GameFightShowFighterMessage import GameFightShowFighterMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterInformations import GameFightFighterInformations
    


class GameFightShowFighterRandomStaticPoseMessage(GameFightShowFighterMessage):
    

    def init(self, informations_:'GameFightFighterInformations'):
        
        super().__init__(informations_)
    
    