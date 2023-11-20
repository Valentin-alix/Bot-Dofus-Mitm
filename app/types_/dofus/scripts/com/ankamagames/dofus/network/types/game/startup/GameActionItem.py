from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.ObjectItemInformationWithQuantity import ObjectItemInformationWithQuantity
class GameActionItem:
	def __init__(self, uid:int, title:str, text:str, descUrl:str, pictureUrl:str, items:list[ObjectItemInformationWithQuantity]):
		self.uid=uid
		self.title=title
		self.text=text
		self.descUrl=descUrl
		self.pictureUrl=pictureUrl
		self.items=items