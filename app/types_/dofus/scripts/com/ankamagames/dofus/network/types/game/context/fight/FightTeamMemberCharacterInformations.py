from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.FightTeamMemberInformations import FightTeamMemberInformations
if TYPE_CHECKING:
	...
class FightTeamMemberCharacterInformations(FightTeamMemberInformations):
	def __init__(self, name:str, level:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.name=name
		self.level=level