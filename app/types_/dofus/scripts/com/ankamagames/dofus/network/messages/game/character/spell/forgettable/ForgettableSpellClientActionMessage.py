from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class ForgettableSpellClientActionMessage:
	def __init__(self, spellId:int, action:int):
		self.spellId=spellId
		self.action=action