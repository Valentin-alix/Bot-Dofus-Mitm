from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.FightTeamMemberCharacterInformations import FightTeamMemberCharacterInformations
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.BasicAllianceInformations import BasicAllianceInformations
class FightTeamMemberWithAllianceCharacterInformations(FightTeamMemberCharacterInformations):
	def __init__(self, allianceInfos:BasicAllianceInformations, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.allianceInfos=allianceInfos