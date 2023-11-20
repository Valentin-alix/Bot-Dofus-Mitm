from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class PaddockInformations:
	def __init__(self, maxOutdoorMount:int, maxItems:int):
		self.maxOutdoorMount=maxOutdoorMount
		self.maxItems=maxItems