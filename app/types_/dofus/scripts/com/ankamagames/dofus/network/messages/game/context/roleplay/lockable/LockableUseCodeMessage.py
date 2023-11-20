from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class LockableUseCodeMessage:
	def __init__(self, code:str):
		self.code=code