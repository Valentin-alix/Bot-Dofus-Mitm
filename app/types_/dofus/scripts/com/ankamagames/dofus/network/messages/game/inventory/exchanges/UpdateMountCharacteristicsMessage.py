from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.mount.UpdateMountCharacteristic import UpdateMountCharacteristic
class UpdateMountCharacteristicsMessage:
	def __init__(self, rideId:int, boostToUpdateList:list[UpdateMountCharacteristic]):
		self.rideId=rideId
		self.boostToUpdateList=boostToUpdateList