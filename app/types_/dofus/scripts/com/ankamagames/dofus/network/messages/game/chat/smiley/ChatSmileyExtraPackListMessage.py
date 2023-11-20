from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ChatSmileyExtraPackListMessage:
	def __init__(self, packIds:list[int]):
		self.packIds=packIds