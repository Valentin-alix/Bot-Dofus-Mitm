from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.connection.IdentificationFailedMessage import IdentificationFailedMessage
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.version.Version import Version
class IdentificationFailedForBadVersionMessage(IdentificationFailedMessage):
	def __init__(self, requiredVersion:Version, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.requiredVersion=requiredVersion