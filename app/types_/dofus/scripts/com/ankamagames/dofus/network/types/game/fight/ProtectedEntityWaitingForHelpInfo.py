from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ProtectedEntityWaitingForHelpInfo:
	def __init__(self, timeLeftBeforeFight:int, waitTimeForPlacement:int, nbPositionForDefensors:int):
		self.timeLeftBeforeFight=timeLeftBeforeFight
		self.waitTimeForPlacement=waitTimeForPlacement
		self.nbPositionForDefensors=nbPositionForDefensors