from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class PopupWarningMessage:
	def __init__(self, lockDuration:int, author:str, content:str):
		self.lockDuration=lockDuration
		self.author=author
		self.content=content