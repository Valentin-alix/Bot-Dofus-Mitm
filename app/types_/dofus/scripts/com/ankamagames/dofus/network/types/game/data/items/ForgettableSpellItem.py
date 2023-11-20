from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.SpellItem import SpellItem
if TYPE_CHECKING:
	...
class ForgettableSpellItem(SpellItem):
	def __init__(self, available:bool, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.available=available