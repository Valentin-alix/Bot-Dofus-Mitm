from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.ObjectItemGenericQuantity import ObjectItemGenericQuantity
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
class ExchangeTaxCollectorGetMessage:
	def __init__(self, collectorName:str, worldX:int, worldY:int, mapId:float, subAreaId:int, userName:str, callerId:int, callerName:str, pods:int, objectsInfos:list[ObjectItemGenericQuantity], look:EntityLook):
		self.collectorName=collectorName
		self.worldX=worldX
		self.worldY=worldY
		self.mapId=mapId
		self.subAreaId=subAreaId
		self.userName=userName
		self.callerId=callerId
		self.callerName=callerName
		self.pods=pods
		self.objectsInfos=objectsInfos
		self.look=look