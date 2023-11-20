from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.FightTeamLightInformations import FightTeamLightInformations
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.FightOptionsInformations import FightOptionsInformations
class FightExternalInformations:
	def __init__(self, fightId:int, fightType:int, fightStart:int, fightSpectatorLocked:bool, fightTeams:list[FightTeamLightInformations], fightTeamsOptions:list[FightOptionsInformations]):
		self.fightId=fightId
		self.fightType=fightType
		self.fightStart=fightStart
		self.fightSpectatorLocked=fightSpectatorLocked
		self.fightTeams=fightTeams
		self.fightTeamsOptions=fightTeamsOptions