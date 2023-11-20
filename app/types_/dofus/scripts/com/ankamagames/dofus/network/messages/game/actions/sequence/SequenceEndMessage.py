from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class SequenceEndMessage:
	def __init__(self, actionId:int, authorId:float, sequenceType:int):
		self.actionId=actionId
		self.authorId=authorId
		self.sequenceType=sequenceType