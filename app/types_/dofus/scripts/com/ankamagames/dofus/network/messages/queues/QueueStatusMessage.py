from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class QueueStatusMessage:
	def __init__(self, position:int, total:int):
		self.position=position
		self.total=total