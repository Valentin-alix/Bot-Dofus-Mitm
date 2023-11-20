from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.collector.tax.TaxCollectorOrderedSpell import TaxCollectorOrderedSpell
class TaxCollectorPresetSpellUpdatedMessage:
	def __init__(self, presetId:int, taxCollectorSpells:list[TaxCollectorOrderedSpell]):
		self.presetId=presetId
		self.taxCollectorSpells=taxCollectorSpells