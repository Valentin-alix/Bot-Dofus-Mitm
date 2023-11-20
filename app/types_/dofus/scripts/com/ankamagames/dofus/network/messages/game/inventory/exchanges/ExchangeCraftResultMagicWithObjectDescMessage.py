from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeCraftResultWithObjectDescMessage import ExchangeCraftResultWithObjectDescMessage
if TYPE_CHECKING:
	...
class ExchangeCraftResultMagicWithObjectDescMessage(ExchangeCraftResultWithObjectDescMessage):
	def __init__(self, magicPoolStatus:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.magicPoolStatus=magicPoolStatus