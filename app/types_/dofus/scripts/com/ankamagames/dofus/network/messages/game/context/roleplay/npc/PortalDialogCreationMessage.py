from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.context.roleplay.npc.NpcDialogCreationMessage import NpcDialogCreationMessage
if TYPE_CHECKING:
	...
class PortalDialogCreationMessage(NpcDialogCreationMessage):
	def __init__(self, type:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.type=type