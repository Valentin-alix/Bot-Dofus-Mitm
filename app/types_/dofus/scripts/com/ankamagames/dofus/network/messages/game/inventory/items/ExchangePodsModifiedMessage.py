from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeObjectMessage import ExchangeObjectMessage
if TYPE_CHECKING:
	...
class ExchangePodsModifiedMessage(ExchangeObjectMessage):
	def __init__(self, currentWeight:int, maxWeight:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.currentWeight=currentWeight
		self.maxWeight=maxWeight