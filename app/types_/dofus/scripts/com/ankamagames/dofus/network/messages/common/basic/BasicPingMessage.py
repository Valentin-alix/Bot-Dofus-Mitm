from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class BasicPingMessage:
	def __init__(self, quiet:bool):
		self.quiet=quiet