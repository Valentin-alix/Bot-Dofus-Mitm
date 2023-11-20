from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.house.HouseInformations import HouseInformations
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation
class HouseInformationsForGuild(HouseInformations):
	def __init__(self, instanceId:int, secondHand:bool, ownerTag:AccountTagInformation, worldX:int, worldY:int, mapId:float, subAreaId:int, skillListIds:list[int], guildshareParams:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.instanceId=instanceId
		self.secondHand=secondHand
		self.ownerTag=ownerTag
		self.worldX=worldX
		self.worldY=worldY
		self.mapId=mapId
		self.subAreaId=subAreaId
		self.skillListIds=skillListIds
		self.guildshareParams=guildshareParams