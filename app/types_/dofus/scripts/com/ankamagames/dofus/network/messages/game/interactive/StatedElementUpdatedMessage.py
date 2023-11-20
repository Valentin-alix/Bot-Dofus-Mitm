from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.interactive.StatedElement import StatedElement
class StatedElementUpdatedMessage:
	def __init__(self, statedElement:StatedElement):
		self.statedElement=statedElement