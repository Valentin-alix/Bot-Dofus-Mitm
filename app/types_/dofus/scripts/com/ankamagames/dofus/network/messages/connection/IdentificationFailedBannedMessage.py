from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.connection.IdentificationFailedMessage import IdentificationFailedMessage
if TYPE_CHECKING:
	...
class IdentificationFailedBannedMessage(IdentificationFailedMessage):
	def __init__(self, banEndDate:float, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.banEndDate=banEndDate