from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.presets.PresetsContainerPreset import PresetsContainerPreset
if TYPE_CHECKING:
	...
class IconNamedPreset(PresetsContainerPreset):
	def __init__(self, iconId:int, name:str, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.iconId=iconId
		self.name=name