from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.Item import Item
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect
class ObjectItemMinimalInformation(Item):
	def __init__(self, objectGID:int, effects:list[ObjectEffect], *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.objectGID=objectGID
		self.effects=effects