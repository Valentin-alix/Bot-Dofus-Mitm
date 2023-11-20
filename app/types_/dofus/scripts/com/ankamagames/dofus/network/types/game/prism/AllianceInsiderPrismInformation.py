from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.prism.PrismInformation import PrismInformation
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem
class AllianceInsiderPrismInformation(PrismInformation):
	def __init__(self, moduleObject:ObjectItem, moduleType:int, cristalObject:ObjectItem, cristalType:int, cristalNumberLeft:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.moduleObject=moduleObject
		self.moduleType=moduleType
		self.cristalObject=cristalObject
		self.cristalType=cristalType
		self.cristalNumberLeft=cristalNumberLeft