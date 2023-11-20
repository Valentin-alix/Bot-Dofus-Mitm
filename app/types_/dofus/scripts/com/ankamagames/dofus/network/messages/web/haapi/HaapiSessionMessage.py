from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class HaapiSessionMessage:
	def __init__(self, key:str, type:int):
		self.key=key
		self.type=type