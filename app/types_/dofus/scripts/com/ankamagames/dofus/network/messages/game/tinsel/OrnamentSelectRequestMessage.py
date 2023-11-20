from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class OrnamentSelectRequestMessage:
	def __init__(self, ornamentId:int):
		self.ornamentId=ornamentId