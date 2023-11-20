from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class AdminCommandMessage:
	def __init__(self, messageUuid:int, content:str):
		self.messageUuid=messageUuid
		self.content=content