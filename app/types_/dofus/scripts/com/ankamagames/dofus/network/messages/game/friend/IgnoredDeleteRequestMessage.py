from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class IgnoredDeleteRequestMessage:
	def __init__(self, accountId:int, session:bool):
		self.accountId=accountId
		self.session=session