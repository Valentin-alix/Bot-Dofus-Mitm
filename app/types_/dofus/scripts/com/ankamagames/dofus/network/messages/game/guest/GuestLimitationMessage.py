from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class GuestLimitationMessage:
	def __init__(self, reason:int):
		self.reason=reason