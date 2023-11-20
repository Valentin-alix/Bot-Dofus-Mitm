from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.IdentifiedEntityDispositionInformations import IdentifiedEntityDispositionInformations
class GameEntityDispositionMessage:
	def __init__(self, disposition:IdentifiedEntityDispositionInformations):
		self.disposition=disposition