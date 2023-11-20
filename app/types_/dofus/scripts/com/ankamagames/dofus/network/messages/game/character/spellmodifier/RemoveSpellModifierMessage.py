from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	...
class RemoveSpellModifierMessage:
	def __init__(self, actorId:float, actionType:int, modifierType:int, spellId:int):
		self.actorId=actorId
		self.actionType=actionType
		self.modifierType=modifierType
		self.spellId=spellId