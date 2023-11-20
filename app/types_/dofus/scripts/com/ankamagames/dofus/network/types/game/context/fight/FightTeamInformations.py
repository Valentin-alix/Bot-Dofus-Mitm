from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.AbstractFightTeamInformations import AbstractFightTeamInformations
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.FightTeamMemberInformations import FightTeamMemberInformations
class FightTeamInformations(AbstractFightTeamInformations):
	def __init__(self, teamMembers:list[FightTeamMemberInformations], *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.teamMembers=teamMembers