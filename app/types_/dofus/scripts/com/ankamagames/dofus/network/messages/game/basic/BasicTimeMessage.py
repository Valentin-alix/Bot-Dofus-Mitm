from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class BasicTimeMessage:
	def __init__(self, timestamp:float, timezoneOffset:int):
		self.timestamp=timestamp
		self.timezoneOffset=timezoneOffset