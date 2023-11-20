from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class AnomalyStateMessage:
	def __init__(self, subAreaId:int, open:bool, closingTime:int):
		self.subAreaId=subAreaId
		self.open=open
		self.closingTime=closingTime