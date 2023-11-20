from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class SocialEmblem:
	def __init__(self, symbolShape:int, symbolColor:int, backgroundShape:int, backgroundColor:int):
		self.symbolShape=symbolShape
		self.symbolColor=symbolColor
		self.backgroundShape=backgroundShape
		self.backgroundColor=backgroundColor