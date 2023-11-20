from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class SpellVariantActivationMessage:
	def __init__(self, spellId:int, result:bool):
		self.spellId=spellId
		self.result=result