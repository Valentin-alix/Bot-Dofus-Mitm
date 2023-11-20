from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class StatedElement:
	def __init__(self, elementId:int, elementCellId:int, elementState:int, onCurrentMap:bool):
		self.elementId=elementId
		self.elementCellId=elementCellId
		self.elementState=elementState
		self.onCurrentMap=onCurrentMap