from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.authorized.AdminCommandMessage import AdminCommandMessage
if TYPE_CHECKING:
	...
class AdminQuietCommandMessage(AdminCommandMessage):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		...