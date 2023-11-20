from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class MountFeedRequestMessage:
	def __init__(self, mountUid:int, mountLocation:int, mountFoodUid:int, quantity:int):
		self.mountUid=mountUid
		self.mountLocation=mountLocation
		self.mountFoodUid=mountFoodUid
		self.quantity=quantity