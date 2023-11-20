from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class PaddockInformationsForSell:
	def __init__(self, guildOwner:str, worldX:int, worldY:int, subAreaId:int, nbMount:int, nbObject:int, price:int):
		self.guildOwner=guildOwner
		self.worldX=worldX
		self.worldY=worldY
		self.subAreaId=subAreaId
		self.nbMount=nbMount
		self.nbObject=nbObject
		self.price=price