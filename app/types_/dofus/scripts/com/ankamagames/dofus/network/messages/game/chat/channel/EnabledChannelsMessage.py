from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class EnabledChannelsMessage:
	def __init__(self, channels:list[int], disallowed:list[int]):
		self.channels=channels
		self.disallowed=disallowed