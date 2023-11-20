from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeObjectMessage import ExchangeObjectMessage
if TYPE_CHECKING:
	...
class ExchangeKamaModifiedMessage(ExchangeObjectMessage):
	def __init__(self, quantity:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.quantity=quantity