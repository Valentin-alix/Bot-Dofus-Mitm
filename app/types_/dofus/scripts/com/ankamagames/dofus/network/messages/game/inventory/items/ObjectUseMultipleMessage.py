from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.items.ObjectUseMessage import ObjectUseMessage
if TYPE_CHECKING:
	...
class ObjectUseMultipleMessage(ObjectUseMessage):
	def __init__(self, quantity:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.quantity=quantity