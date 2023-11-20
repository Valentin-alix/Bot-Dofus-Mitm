from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ForceAccountMessage:
	def __init__(self, accountId:int):
		self.accountId=accountId