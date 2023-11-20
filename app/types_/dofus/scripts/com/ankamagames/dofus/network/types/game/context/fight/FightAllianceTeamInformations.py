from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.FightTeamInformations import FightTeamInformations
if TYPE_CHECKING:
	...
class FightAllianceTeamInformations(FightTeamInformations):
	def __init__(self, relation:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.relation=relation