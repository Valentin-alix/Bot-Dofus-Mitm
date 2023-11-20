from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class SpellForPreset:
	def __init__(self, spellId:int, shortcuts:list[int]):
		self.spellId=spellId
		self.shortcuts=shortcuts