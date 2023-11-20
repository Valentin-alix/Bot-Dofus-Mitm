from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameFightPlacementSwapPositionsCancelledMessage:
	def __init__(self, requestId:int, cancellerId:float):
		self.requestId=requestId
		self.cancellerId=cancellerId