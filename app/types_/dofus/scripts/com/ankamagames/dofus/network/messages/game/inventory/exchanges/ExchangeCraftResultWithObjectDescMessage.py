from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeCraftResultMessage import ExchangeCraftResultMessage
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.ObjectItemNotInContainer import ObjectItemNotInContainer
class ExchangeCraftResultWithObjectDescMessage(ExchangeCraftResultMessage):
	def __init__(self, objectInfo:ObjectItemNotInContainer, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.objectInfo=objectInfo