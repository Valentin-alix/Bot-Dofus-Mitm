from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.presets.ItemForPreset import ItemForPreset
class ItemForPresetUpdateMessage:
	def __init__(self, presetId:int, presetItem:ItemForPreset):
		self.presetId=presetId
		self.presetItem=presetItem