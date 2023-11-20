from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ChatAbstractClientMessage:
	def __init__(self, content:str):
		self.content=content