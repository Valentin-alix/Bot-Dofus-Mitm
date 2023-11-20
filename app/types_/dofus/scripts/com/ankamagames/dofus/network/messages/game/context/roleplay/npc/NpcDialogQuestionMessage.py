from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class NpcDialogQuestionMessage:
	def __init__(self, messageId:int, dialogParams:list[str], visibleReplies:list[int]):
		self.messageId=messageId
		self.dialogParams=dialogParams
		self.visibleReplies=visibleReplies