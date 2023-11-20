from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.spellmodifier.SpellModifierMessage import SpellModifierMessage
class ApplySpellModifierMessage:
	def __init__(self, actorId:float, modifier:SpellModifierMessage):
		self.actorId=actorId
		self.modifier=modifier