from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class FightPhase:
	def __init__(self, phase:int, phaseEndTimeStamp:float):
		self.phase=phase
		self.phaseEndTimeStamp=phaseEndTimeStamp