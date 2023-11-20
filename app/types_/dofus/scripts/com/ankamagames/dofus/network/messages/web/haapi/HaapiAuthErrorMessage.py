from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class HaapiAuthErrorMessage:
	def __init__(self, type:int):
		self.type=type