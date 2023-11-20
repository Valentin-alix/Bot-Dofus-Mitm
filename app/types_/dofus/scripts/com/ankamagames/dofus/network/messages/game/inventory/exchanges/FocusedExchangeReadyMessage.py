from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeReadyMessage import ExchangeReadyMessage
if TYPE_CHECKING:
	...
class FocusedExchangeReadyMessage(ExchangeReadyMessage):
	def __init__(self, focusActionId:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.focusActionId=focusActionId