from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.GoldItem import GoldItem
class GoldAddedMessage:
	def __init__(self, gold:GoldItem):
		self.gold=gold