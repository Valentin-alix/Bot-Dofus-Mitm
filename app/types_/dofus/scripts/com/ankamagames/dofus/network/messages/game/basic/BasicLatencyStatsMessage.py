from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class BasicLatencyStatsMessage:
	def __init__(self, latency:int, sampleCount:int, max:int):
		self.latency=latency
		self.sampleCount=sampleCount
		self.max=max