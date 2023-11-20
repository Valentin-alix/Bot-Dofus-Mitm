from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeBidHouseInListAddedMessage import ExchangeBidHouseInListAddedMessage
if TYPE_CHECKING:
	...
class ExchangeBidHouseInListUpdatedMessage(ExchangeBidHouseInListAddedMessage):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		...