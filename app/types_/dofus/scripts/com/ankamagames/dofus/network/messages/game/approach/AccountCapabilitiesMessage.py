from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class AccountCapabilitiesMessage:
	def __init__(self, accountId:int, status:int):
		self.accountId=accountId
		self.status=status