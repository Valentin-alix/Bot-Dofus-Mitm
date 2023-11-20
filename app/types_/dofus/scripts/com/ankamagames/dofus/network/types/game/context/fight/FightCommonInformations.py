from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.FightTeamInformations import FightTeamInformations
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.FightOptionsInformations import FightOptionsInformations
class FightCommonInformations:
	def __init__(self, fightId:int, fightType:int, fightTeams:list[FightTeamInformations], fightTeamsPositions:list[int], fightTeamsOptions:list[FightOptionsInformations]):
		self.fightId=fightId
		self.fightType=fightType
		self.fightTeams=fightTeams
		self.fightTeamsPositions=fightTeamsPositions
		self.fightTeamsOptions=fightTeamsOptions