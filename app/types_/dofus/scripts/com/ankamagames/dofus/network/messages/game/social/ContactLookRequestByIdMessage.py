from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.social.ContactLookRequestMessage import ContactLookRequestMessage
if TYPE_CHECKING:
	...
class ContactLookRequestByIdMessage(ContactLookRequestMessage):
	def __init__(self, playerId:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.playerId=playerId