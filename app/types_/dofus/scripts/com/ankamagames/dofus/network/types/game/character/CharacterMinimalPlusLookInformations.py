from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
class CharacterMinimalPlusLookInformations(CharacterMinimalInformations):
	def __init__(self, entityLook:EntityLook, breed:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.entityLook=entityLook
		self.breed=breed