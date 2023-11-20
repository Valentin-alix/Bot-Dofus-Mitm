from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class TextInformationMessage:
	def __init__(self, msgType:int, msgId:int, parameters:list[str]):
		self.msgType=msgType
		self.msgId=msgId
		self.parameters=parameters