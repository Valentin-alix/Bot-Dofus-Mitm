from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.prism.PrismInformation import PrismInformation
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.AllianceInformation import AllianceInformation
class AlliancePrismInformation(PrismInformation):
	def __init__(self, alliance:AllianceInformation, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.alliance=alliance