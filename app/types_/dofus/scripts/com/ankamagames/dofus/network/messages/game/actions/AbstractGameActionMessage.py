from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class AbstractGameActionMessage:
	def __init__(self, actionId:int, sourceId:float):
		self.actionId=actionId
		self.sourceId=sourceId