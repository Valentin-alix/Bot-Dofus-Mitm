from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.AbstractFightTeamInformations import AbstractFightTeamInformations
if TYPE_CHECKING:
	...
class FightTeamLightInformations(AbstractFightTeamInformations):
	def __init__(self, teamMembersCount:int, meanLevel:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.teamMembersCount=teamMembersCount
		self.meanLevel=meanLevel