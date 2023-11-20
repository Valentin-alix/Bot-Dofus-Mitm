from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.presets.IconPresetSaveRequestMessage import IconPresetSaveRequestMessage
if TYPE_CHECKING:
	...
class IconNamedPresetSaveRequestMessage(IconPresetSaveRequestMessage):
	def __init__(self, name:str, type:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.name=name
		self.type=type