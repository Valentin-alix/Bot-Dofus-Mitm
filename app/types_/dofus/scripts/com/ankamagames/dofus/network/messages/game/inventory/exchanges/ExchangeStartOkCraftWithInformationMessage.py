from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeStartOkCraftMessage import ExchangeStartOkCraftMessage
if TYPE_CHECKING:
	...
class ExchangeStartOkCraftWithInformationMessage(ExchangeStartOkCraftMessage):
	def __init__(self, skillId:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.skillId=skillId