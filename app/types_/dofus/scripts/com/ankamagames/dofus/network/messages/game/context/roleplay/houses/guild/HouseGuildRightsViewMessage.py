from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class HouseGuildRightsViewMessage:
	def __init__(self, houseId:int, instanceId:int):
		self.houseId=houseId
		self.instanceId=instanceId