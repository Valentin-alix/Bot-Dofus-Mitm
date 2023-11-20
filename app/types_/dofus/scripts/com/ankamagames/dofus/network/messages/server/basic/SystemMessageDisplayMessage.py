from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class SystemMessageDisplayMessage:
	def __init__(self, hangUp:bool, msgId:int, parameters:list[str]):
		self.hangUp=hangUp
		self.msgId=msgId
		self.parameters=parameters