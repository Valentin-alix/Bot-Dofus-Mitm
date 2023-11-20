from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.interactive.InteractiveElement import InteractiveElement
class InteractiveElementUpdatedMessage:
	def __init__(self, interactiveElement:InteractiveElement):
		self.interactiveElement=interactiveElement