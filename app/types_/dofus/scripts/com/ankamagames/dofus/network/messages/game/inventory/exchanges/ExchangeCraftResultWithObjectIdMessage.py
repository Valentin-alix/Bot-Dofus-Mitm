from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeCraftResultMessage import ExchangeCraftResultMessage
if TYPE_CHECKING:
	...
class ExchangeCraftResultWithObjectIdMessage(ExchangeCraftResultMessage):
	def __init__(self, objectGenericId:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.objectGenericId=objectGenericId