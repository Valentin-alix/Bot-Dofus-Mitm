from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeRequestedMessage import ExchangeRequestedMessage
if TYPE_CHECKING:
	...
class ExchangeRequestedTradeMessage(ExchangeRequestedMessage):
	def __init__(self, source:int, target:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.source=source
		self.target=target