from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeObjectMoveMessage import ExchangeObjectMoveMessage
if TYPE_CHECKING:
	...
class ExchangeObjectMovePricedMessage(ExchangeObjectMoveMessage):
	def __init__(self, price:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.price=price