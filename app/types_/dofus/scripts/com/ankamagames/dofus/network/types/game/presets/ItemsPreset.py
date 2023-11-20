from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.presets.Preset import Preset
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.presets.ItemForPreset import ItemForPreset
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
class ItemsPreset(Preset):
	def __init__(self, items:list[ItemForPreset], mountEquipped:bool, look:EntityLook, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.items=items
		self.mountEquipped=mountEquipped
		self.look=look