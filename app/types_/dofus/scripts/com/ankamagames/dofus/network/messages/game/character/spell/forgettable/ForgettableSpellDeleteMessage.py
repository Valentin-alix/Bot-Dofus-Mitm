from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ForgettableSpellDeleteMessage:
	def __init__(self, reason:int, spells:list[int]):
		self.reason=reason
		self.spells=spells