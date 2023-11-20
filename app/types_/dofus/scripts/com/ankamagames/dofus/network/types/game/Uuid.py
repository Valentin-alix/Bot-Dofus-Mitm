from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class Uuid:
	def __init__(self, uuidString:str):
		self.uuidString=uuidString