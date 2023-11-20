from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.collector.tax.TaxCollectorComplementaryInformations import TaxCollectorComplementaryInformations
if TYPE_CHECKING:
	...
class TaxCollectorLootInformations(TaxCollectorComplementaryInformations):
	def __init__(self, pods:int, itemsValue:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.pods=pods
		self.itemsValue=itemsValue