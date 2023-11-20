from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.presets.Preset import Preset
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.presets.CharacterCharacteristicForPreset import CharacterCharacteristicForPreset
class FullStatsPreset(Preset):
	def __init__(self, stats:list[CharacterCharacteristicForPreset], *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.stats=stats