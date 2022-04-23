from com.ankamagames.dofus.logic.game.roleplay.types.FightTeam import FightTeam
from com.ankamagames.jerakine.logger.Logger import Logger

logger = Logger(__name__)


class Fight:

    fightId: int

    teams: list[FightTeam]

    def __init__(self, fightId: int, teams: list[FightTeam]):
        super().__init__()
        self.fightId = fightId
        self.teams = teams

    def getTeamByType(self, teamType: int) -> FightTeam:
        team: FightTeam = None
        for team in self.teams:
            if team.teamType == teamType:
                return team
        return None

    def getTeamById(self, teamId: int) -> FightTeam:
        team: FightTeam = None
        for team in self.teams:
            if team.teamInfos.teamId == teamId:
                return team
        return None
