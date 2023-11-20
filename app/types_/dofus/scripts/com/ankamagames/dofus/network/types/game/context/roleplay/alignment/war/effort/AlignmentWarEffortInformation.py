from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class AlignmentWarEffortInformation:
	def __init__(self, alignmentSide:int, alignmentWarEffort:int):
		self.alignmentSide=alignmentSide
		self.alignmentWarEffort=alignmentWarEffort