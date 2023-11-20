from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class TaxCollectorStateUpdateMessage:
	def __init__(self, uniqueId:float, state:int):
		self.uniqueId=uniqueId
		self.state=state