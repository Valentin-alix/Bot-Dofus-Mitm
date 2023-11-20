from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ProtocolRequired:
	def __init__(self, version:str):
		self.version=version