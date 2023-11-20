from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.collector.tax.TaxCollectorPreset import TaxCollectorPreset
class TaxCollectorPresetsMessage:
	def __init__(self, presets:list[TaxCollectorPreset]):
		self.presets=presets