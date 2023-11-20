from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class EmoteListMessage:
	def __init__(self, emoteIds:list[int]):
		self.emoteIds=emoteIds