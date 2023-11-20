from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class AccountLoggingKickedMessage:
	def __init__(self, days:int, hours:int, minutes:int):
		self.days=days
		self.hours=hours
		self.minutes=minutes