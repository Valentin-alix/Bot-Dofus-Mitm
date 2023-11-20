from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeRequestMessage import ExchangeRequestMessage
if TYPE_CHECKING:
	...
class ExchangePlayerMultiCraftRequestMessage(ExchangeRequestMessage):
	def __init__(self, target:int, skillId:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.target=target
		self.skillId=skillId