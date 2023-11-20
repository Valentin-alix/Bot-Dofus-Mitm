from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.collector.tax.TaxCollectorOrderedSpell import TaxCollectorOrderedSpell
class AddTaxCollectorPresetSpellMessage:
	def __init__(self, presetId:int, spell:TaxCollectorOrderedSpell):
		self.presetId=presetId
		self.spell=spell