from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class CheckFileMessage:
	def __init__(self, filenameHash:str, type:int, value:str):
		self.filenameHash=filenameHash
		self.type=type
		self.value=value