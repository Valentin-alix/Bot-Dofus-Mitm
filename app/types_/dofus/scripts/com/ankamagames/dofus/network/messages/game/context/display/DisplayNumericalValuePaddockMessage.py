from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class DisplayNumericalValuePaddockMessage:
	def __init__(self, rideId:int, value:int, type:int):
		self.rideId=rideId
		self.value=value
		self.type=type