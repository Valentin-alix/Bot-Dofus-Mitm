from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations
class GameContextActorPositionInformations:
	def __init__(self, contextualId:float, disposition:EntityDispositionInformations):
		self.contextualId=contextualId
		self.disposition=disposition