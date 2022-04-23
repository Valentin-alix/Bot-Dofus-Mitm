from com.ankamagames.dofus.network.messages.game.context.fight.GameFightJoinMessage import GameFightJoinMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.party.NamedPartyTeam import NamedPartyTeam
    


class GameFightSpectatorJoinMessage(GameFightJoinMessage):
    namedPartyTeams:list['NamedPartyTeam']
    

    def init(self, namedPartyTeams_:list['NamedPartyTeam'], timeMaxBeforeFightStart_:int, fightType_:int, isTeamPhase_:bool, canBeCancelled_:bool, canSayReady_:bool, isFightStarted_:bool):
        self.namedPartyTeams = namedPartyTeams_
        
        super().__init__(timeMaxBeforeFightStart_, fightType_, isTeamPhase_, canBeCancelled_, canSayReady_, isFightStarted_)
    
    