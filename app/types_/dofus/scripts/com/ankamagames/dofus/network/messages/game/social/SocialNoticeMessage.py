from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class SocialNoticeMessage:
	def __init__(self, content:str, timestamp:int, memberId:int, memberName:str):
		self.content=content
		self.timestamp=timestamp
		self.memberId=memberId
		self.memberName=memberName