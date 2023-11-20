from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.debug.DebugInClientMessage import DebugInClientMessage
if TYPE_CHECKING:
	...
class ClientYouAreDrunkMessage(DebugInClientMessage):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		...