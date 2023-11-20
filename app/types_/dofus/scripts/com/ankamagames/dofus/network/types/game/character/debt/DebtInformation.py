from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class DebtInformation:
	def __init__(self, id:float, timestamp:float):
		self.id=id
		self.timestamp=timestamp