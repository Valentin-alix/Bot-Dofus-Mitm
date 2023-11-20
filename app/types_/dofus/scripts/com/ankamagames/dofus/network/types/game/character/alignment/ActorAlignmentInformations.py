from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ActorAlignmentInformations:
	def __init__(self, alignmentSide:int, alignmentValue:int, alignmentGrade:int, characterPower:float):
		self.alignmentSide=alignmentSide
		self.alignmentValue=alignmentValue
		self.alignmentGrade=alignmentGrade
		self.characterPower=characterPower