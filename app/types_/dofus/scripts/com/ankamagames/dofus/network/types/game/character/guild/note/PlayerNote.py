from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class PlayerNote:
	def __init__(self, content:str, lastEditDate:float):
		self.content=content
		self.lastEditDate=lastEditDate