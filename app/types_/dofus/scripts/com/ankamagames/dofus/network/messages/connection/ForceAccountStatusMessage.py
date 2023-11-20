from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ForceAccountStatusMessage:
	def __init__(self, force:bool, forcedAccountId:int, forcedNickname:str, forcedTag:str):
		self.force=force
		self.forcedAccountId=forcedAccountId
		self.forcedNickname=forcedNickname
		self.forcedTag=forcedTag