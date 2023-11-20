from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.presets.Preset import Preset
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.presets.SimpleCharacterCharacteristicForPreset import SimpleCharacterCharacteristicForPreset
class StatsPreset(Preset):
	def __init__(self, stats:list[SimpleCharacterCharacteristicForPreset], *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.stats=stats