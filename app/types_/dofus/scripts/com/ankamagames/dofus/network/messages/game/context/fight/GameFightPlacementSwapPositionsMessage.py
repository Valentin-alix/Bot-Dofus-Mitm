from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.IdentifiedEntityDispositionInformations import IdentifiedEntityDispositionInformations
class GameFightPlacementSwapPositionsMessage:
	def __init__(self, dispositions:list[IdentifiedEntityDispositionInformations]):
		self.dispositions=dispositions