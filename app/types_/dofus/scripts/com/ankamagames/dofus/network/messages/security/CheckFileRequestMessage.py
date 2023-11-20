from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class CheckFileRequestMessage:
	def __init__(self, filename:str, type:int):
		self.filename=filename
		self.type=type