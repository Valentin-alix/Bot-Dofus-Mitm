from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.presets.Preset import Preset
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.presets.SpellForPreset import SpellForPreset
class SpellsPreset(Preset):
	def __init__(self, spells:list[SpellForPreset], *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.spells=spells