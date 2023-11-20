from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.FightResultListEntry import FightResultListEntry
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.party.NamedPartyTeamWithOutcome import NamedPartyTeamWithOutcome
class GameFightEndMessage:
	def __init__(self, duration:int, rewardRate:int, lootShareLimitMalus:int, results:list[FightResultListEntry], namedPartyTeamsOutcomes:list[NamedPartyTeamWithOutcome]):
		self.duration=duration
		self.rewardRate=rewardRate
		self.lootShareLimitMalus=lootShareLimitMalus
		self.results=results
		self.namedPartyTeamsOutcomes=namedPartyTeamsOutcomes