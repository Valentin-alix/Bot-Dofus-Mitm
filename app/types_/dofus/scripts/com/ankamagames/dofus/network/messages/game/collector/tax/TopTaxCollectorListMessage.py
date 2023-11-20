from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.collector.tax.TaxCollectorInformations import TaxCollectorInformations
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.collector.tax.TaxCollectorInformations import TaxCollectorInformations
class TopTaxCollectorListMessage:
	def __init__(self, dungeonTaxCollectorsInformation:list[TaxCollectorInformations], worldTaxCollectorsInformation:list[TaxCollectorInformations]):
		self.dungeonTaxCollectorsInformation=dungeonTaxCollectorsInformation
		self.worldTaxCollectorsInformation=worldTaxCollectorsInformation