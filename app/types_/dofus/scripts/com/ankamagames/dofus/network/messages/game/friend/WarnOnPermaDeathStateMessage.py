from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class WarnOnPermaDeathStateMessage:
	def __init__(self, enable:bool):
		self.enable=enable