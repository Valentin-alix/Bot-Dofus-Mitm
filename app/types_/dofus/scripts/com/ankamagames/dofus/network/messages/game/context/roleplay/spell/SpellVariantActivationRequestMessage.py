from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class SpellVariantActivationRequestMessage:
	def __init__(self, spellId:int):
		self.spellId=spellId