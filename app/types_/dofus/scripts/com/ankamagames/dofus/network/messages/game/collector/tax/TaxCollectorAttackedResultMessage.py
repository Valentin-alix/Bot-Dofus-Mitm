from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.collector.tax.TaxCollectorBasicInformations import TaxCollectorBasicInformations
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.BasicAllianceInformations import BasicAllianceInformations
class TaxCollectorAttackedResultMessage:
	def __init__(self, deadOrAlive:bool, basicInfos:TaxCollectorBasicInformations, alliance:BasicAllianceInformations):
		self.deadOrAlive=deadOrAlive
		self.basicInfos=basicInfos
		self.alliance=alliance