from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.paddock.PaddockItem import PaddockItem
class GameDataPaddockObjectListAddMessage:
	def __init__(self, paddockItemDescription:list[PaddockItem]):
		self.paddockItemDescription=paddockItemDescription