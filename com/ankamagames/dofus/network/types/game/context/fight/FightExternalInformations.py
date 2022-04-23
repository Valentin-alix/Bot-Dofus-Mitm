from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.fight.FightTeamLightInformations import FightTeamLightInformations
    from com.ankamagames.dofus.network.types.game.context.fight.FightOptionsInformations import FightOptionsInformations
    


class FightExternalInformations(NetworkMessage):
    fightId:int
    fightType:int
    fightStart:int
    fightSpectatorLocked:bool
    fightTeams:list['FightTeamLightInformations']
    fightTeamsOptions:list['FightOptionsInformations']
    

    def init(self, fightId_:int, fightType_:int, fightStart_:int, fightSpectatorLocked_:bool, fightTeams_:list['FightTeamLightInformations'], fightTeamsOptions_:list['FightOptionsInformations']):
        self.fightId = fightId_
        self.fightType = fightType_
        self.fightStart = fightStart_
        self.fightSpectatorLocked = fightSpectatorLocked_
        self.fightTeams = fightTeams_
        self.fightTeamsOptions = fightTeamsOptions_
        
        super().__init__()
    
    