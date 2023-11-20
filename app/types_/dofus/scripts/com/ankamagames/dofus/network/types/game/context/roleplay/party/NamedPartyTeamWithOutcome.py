from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.party.NamedPartyTeam import NamedPartyTeam
class NamedPartyTeamWithOutcome:
	def __init__(self, team:NamedPartyTeam, outcome:int):
		self.team=team
		self.outcome=outcome