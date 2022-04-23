from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.fight.arena.LeagueFriendInformations import LeagueFriendInformations
    


class GameRolePlayArenaInvitationCandidatesAnswerMessage(NetworkMessage):
    candidates:list['LeagueFriendInformations']
    

    def init(self, candidates_:list['LeagueFriendInformations']):
        self.candidates = candidates_
        
        super().__init__()
    
    