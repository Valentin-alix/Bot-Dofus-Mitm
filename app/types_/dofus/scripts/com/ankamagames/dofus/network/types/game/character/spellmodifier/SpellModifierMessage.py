from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class SpellModifierMessage:
	def __init__(self, spellId:int, actionType:int, modifierType:int, context:int, equipment:int):
		self.spellId=spellId
		self.actionType=actionType
		self.modifierType=modifierType
		self.context=context
		self.equipment=equipment