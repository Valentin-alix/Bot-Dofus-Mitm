from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GuildLogbookEntryBasicInformation:
	def __init__(self, id:int, date:float):
		self.id=id
		self.date=date