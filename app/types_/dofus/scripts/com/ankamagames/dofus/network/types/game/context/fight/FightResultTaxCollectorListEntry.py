from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.FightResultFighterListEntry import FightResultFighterListEntry
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.BasicAllianceInformations import BasicAllianceInformations
class FightResultTaxCollectorListEntry(FightResultFighterListEntry):
	def __init__(self, allianceInfo:BasicAllianceInformations, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.allianceInfo=allianceInfo