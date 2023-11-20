from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.ObjectItemQuantity import ObjectItemQuantity
class ObjectFeedMessage:
	def __init__(self, objectUID:int, meal:list[ObjectItemQuantity]):
		self.objectUID=objectUID
		self.meal=meal