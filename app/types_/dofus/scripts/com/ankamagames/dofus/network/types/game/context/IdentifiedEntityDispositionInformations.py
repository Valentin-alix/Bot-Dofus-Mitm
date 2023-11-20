from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations
if TYPE_CHECKING:
	...
class IdentifiedEntityDispositionInformations(EntityDispositionInformations):
	def __init__(self, id:float, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.id=id