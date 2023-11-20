from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.items.ObtainedItemMessage import ObtainedItemMessage
if TYPE_CHECKING:
	...
class ObtainedItemWithBonusMessage(ObtainedItemMessage):
	def __init__(self, bonusQuantity:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.bonusQuantity=bonusQuantity