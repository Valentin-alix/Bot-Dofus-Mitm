from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.interactive.InteractiveUseRequestMessage import InteractiveUseRequestMessage
if TYPE_CHECKING:
	...
class InteractiveUseWithParamRequestMessage(InteractiveUseRequestMessage):
	def __init__(self, id:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.id=id