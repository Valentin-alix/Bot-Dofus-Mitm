from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.collector.tax.TaxCollectorOrderedSpell import TaxCollectorOrderedSpell
class TaxCollectorOrderedSpellUpdatedMessage:
	def __init__(self, taxCollectorId:float, taxCollectorSpells:list[TaxCollectorOrderedSpell]):
		self.taxCollectorId=taxCollectorId
		self.taxCollectorSpells=taxCollectorSpells