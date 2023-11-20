from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class SequenceStartMessage:
	def __init__(self, sequenceType:int, authorId:float):
		self.sequenceType=sequenceType
		self.authorId=authorId