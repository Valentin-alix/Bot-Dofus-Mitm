from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class JobAllowMultiCraftRequestMessage:
	def __init__(self, enabled:bool):
		self.enabled=enabled