from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.common.AbstractPlayerSearchInformation import AbstractPlayerSearchInformation
class PartyInvitationRequestMessage:
	def __init__(self, target:AbstractPlayerSearchInformation):
		self.target=target