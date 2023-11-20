from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class OnConnectionEventMessage:
	def __init__(self, eventType:int):
		self.eventType=eventType