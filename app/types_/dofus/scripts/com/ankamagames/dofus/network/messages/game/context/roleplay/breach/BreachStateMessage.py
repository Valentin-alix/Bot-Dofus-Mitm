from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffectInteger import ObjectEffectInteger
class BreachStateMessage:
	def __init__(self, owner:CharacterMinimalInformations, bonuses:list[ObjectEffectInteger], bugdet:int, saved:bool):
		self.owner=owner
		self.bonuses=bonuses
		self.bugdet=bugdet
		self.saved=saved