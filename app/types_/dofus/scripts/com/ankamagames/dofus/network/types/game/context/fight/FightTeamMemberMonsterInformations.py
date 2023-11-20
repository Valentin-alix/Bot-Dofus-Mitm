from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.FightTeamMemberInformations import FightTeamMemberInformations
if TYPE_CHECKING:
	...
class FightTeamMemberMonsterInformations(FightTeamMemberInformations):
	def __init__(self, monsterId:int, grade:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.monsterId=monsterId
		self.grade=grade