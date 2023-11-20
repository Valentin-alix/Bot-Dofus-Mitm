from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class FriendDeleteRequestMessage:
	def __init__(self, accountId:int):
		self.accountId=accountId