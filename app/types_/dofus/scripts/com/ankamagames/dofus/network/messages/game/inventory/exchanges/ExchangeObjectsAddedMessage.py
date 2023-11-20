from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeObjectMessage import ExchangeObjectMessage
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem
class ExchangeObjectsAddedMessage(ExchangeObjectMessage):
	def __init__(self, object:list[ObjectItem], *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.object=object