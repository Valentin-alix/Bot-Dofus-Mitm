from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations
if TYPE_CHECKING:
	...
class FightEntityDispositionInformations(EntityDispositionInformations):
	def __init__(self, carryingCharacterId:float, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.carryingCharacterId=carryingCharacterId