from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartedMessage import ExchangeStartedMessage
if TYPE_CHECKING:
	...
class ExchangeStartedWithStorageMessage(ExchangeStartedMessage):
	def __init__(self, storageMaxSlot:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.storageMaxSlot=storageMaxSlot