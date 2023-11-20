from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeMountsStableAddMessage import ExchangeMountsStableAddMessage
if TYPE_CHECKING:
	...
class ExchangeMountsStableBornAddMessage(ExchangeMountsStableAddMessage):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		...