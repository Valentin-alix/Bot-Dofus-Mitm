from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class CurrentServerStatusUpdateMessage:
	def __init__(self, status:int):
		self.status=status