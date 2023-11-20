from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.finishmoves.FinishMoveInformations import FinishMoveInformations
class FinishMoveListMessage:
	def __init__(self, finishMoves:list[FinishMoveInformations]):
		self.finishMoves=finishMoves