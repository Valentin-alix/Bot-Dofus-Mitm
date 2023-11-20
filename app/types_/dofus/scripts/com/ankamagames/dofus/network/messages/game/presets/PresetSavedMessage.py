from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.presets.Preset import Preset
class PresetSavedMessage:
	def __init__(self, presetId:int, preset:Preset):
		self.presetId=presetId
		self.preset=preset