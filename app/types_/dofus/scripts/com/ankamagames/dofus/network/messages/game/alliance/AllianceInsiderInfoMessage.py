from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.social.AllianceFactSheetInformation import AllianceFactSheetInformation
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.alliance.AllianceMemberInfo import AllianceMemberInfo
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.prism.PrismGeolocalizedInformation import PrismGeolocalizedInformation
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.collector.tax.TaxCollectorInformations import TaxCollectorInformations
class AllianceInsiderInfoMessage:
	def __init__(self, allianceInfos:AllianceFactSheetInformation, members:list[AllianceMemberInfo], prisms:list[PrismGeolocalizedInformation], taxCollectors:list[TaxCollectorInformations]):
		self.allianceInfos=allianceInfos
		self.members=members
		self.prisms=prisms
		self.taxCollectors=taxCollectors