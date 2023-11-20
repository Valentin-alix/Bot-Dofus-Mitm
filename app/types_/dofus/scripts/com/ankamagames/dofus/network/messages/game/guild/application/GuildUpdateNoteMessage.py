from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GuildUpdateNoteMessage:
	def __init__(self, memberId:int, note:str):
		self.memberId=memberId
		self.note=note