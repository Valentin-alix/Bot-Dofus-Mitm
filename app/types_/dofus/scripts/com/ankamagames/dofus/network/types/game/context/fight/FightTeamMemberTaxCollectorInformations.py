from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.FightTeamMemberInformations import FightTeamMemberInformations
if TYPE_CHECKING:
	...
class FightTeamMemberTaxCollectorInformations(FightTeamMemberInformations):
	def __init__(self, firstNameId:int, lastNameId:int, groupId:int, uid:float, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.firstNameId=firstNameId
		self.lastNameId=lastNameId
		self.groupId=groupId
		self.uid=uid