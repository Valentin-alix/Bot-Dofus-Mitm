from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.presets.Preset import Preset
if TYPE_CHECKING:
	...
class EntitiesPreset(Preset):
	def __init__(self, iconId:int, entityIds:list[int], *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.iconId=iconId
		self.entityIds=entityIds