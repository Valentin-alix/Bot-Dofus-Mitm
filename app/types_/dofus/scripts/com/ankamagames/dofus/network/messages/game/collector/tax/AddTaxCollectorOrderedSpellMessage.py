from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.collector.tax.TaxCollectorOrderedSpell import TaxCollectorOrderedSpell
class AddTaxCollectorOrderedSpellMessage:
	def __init__(self, taxCollectorId:float, spell:TaxCollectorOrderedSpell):
		self.taxCollectorId=taxCollectorId
		self.spell=spell