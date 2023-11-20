from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.Item import Item
if TYPE_CHECKING:
	...
class GoldItem(Item):
	def __init__(self, sum:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.sum=sum