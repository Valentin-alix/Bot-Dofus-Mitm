from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GameFightPlacementSwapPositionsOfferMessage:
	def __init__(self, requestId:int, requesterId:float, requesterCellId:int, requestedId:float, requestedCellId:int):
		self.requestId=requestId
		self.requesterId=requesterId
		self.requesterCellId=requesterCellId
		self.requestedId=requestedId
		self.requestedCellId=requestedCellId