from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.presets.Preset import Preset
class PresetsMessage:
	def __init__(self, presets:list[Preset]):
		self.presets=presets