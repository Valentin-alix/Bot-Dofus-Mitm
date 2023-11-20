from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeObjectMessage import ExchangeObjectMessage
if TYPE_CHECKING:
	...
class ExchangeObjectsRemovedMessage(ExchangeObjectMessage):
	def __init__(self, objectUID:list[int], *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.objectUID=objectUID