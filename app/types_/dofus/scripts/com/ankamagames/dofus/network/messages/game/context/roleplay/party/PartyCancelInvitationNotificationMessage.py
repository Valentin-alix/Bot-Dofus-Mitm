from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyEventMessage import AbstractPartyEventMessage
if TYPE_CHECKING:
	...
class PartyCancelInvitationNotificationMessage(AbstractPartyEventMessage):
	def __init__(self, cancelerId:int, guestId:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.cancelerId=cancelerId
		self.guestId=guestId