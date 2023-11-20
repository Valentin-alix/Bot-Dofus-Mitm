from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.shortcut.ShortcutObject import ShortcutObject
if TYPE_CHECKING:
	...
class ShortcutObjectItem(ShortcutObject):
	def __init__(self, itemUID:int, itemGID:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.itemUID=itemUID
		self.itemGID=itemGID