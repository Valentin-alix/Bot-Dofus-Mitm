from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class HouseGuildShareRequestMessage:
	def __init__(self, houseId:int, instanceId:int, enable:bool, rights:int):
		self.houseId=houseId
		self.instanceId=instanceId
		self.enable=enable
		self.rights=rights