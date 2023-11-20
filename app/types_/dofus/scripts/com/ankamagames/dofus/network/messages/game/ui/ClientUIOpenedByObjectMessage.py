from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.ui.ClientUIOpenedMessage import ClientUIOpenedMessage
if TYPE_CHECKING:
	...
class ClientUIOpenedByObjectMessage(ClientUIOpenedMessage):
	def __init__(self, uid:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.uid=uid