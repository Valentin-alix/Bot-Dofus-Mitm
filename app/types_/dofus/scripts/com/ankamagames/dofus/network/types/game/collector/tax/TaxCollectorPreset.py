from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.collector.tax.TaxCollectorOrderedSpell import TaxCollectorOrderedSpell
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristics import CharacterCharacteristics
class TaxCollectorPreset:
	def __init__(self, presetId:int, spells:list[TaxCollectorOrderedSpell], characteristics:CharacterCharacteristics):
		self.presetId=presetId
		self.spells=spells
		self.characteristics=characteristics