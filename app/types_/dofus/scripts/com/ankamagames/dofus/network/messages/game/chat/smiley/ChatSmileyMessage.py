from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ChatSmileyMessage:
	def __init__(self, entityId:float, smileyId:int, accountId:int):
		self.entityId=entityId
		self.smileyId=smileyId
		self.accountId=accountId