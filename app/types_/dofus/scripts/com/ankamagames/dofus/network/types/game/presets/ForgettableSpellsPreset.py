from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.presets.Preset import Preset
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.presets.SpellsPreset import SpellsPreset
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.presets.SpellForPreset import SpellForPreset
class ForgettableSpellsPreset(Preset):
	def __init__(self, baseSpellsPreset:SpellsPreset, forgettableSpells:list[SpellForPreset], *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.baseSpellsPreset=baseSpellsPreset
		self.forgettableSpells=forgettableSpells