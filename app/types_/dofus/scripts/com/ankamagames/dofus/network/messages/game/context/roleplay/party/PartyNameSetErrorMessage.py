from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage
if TYPE_CHECKING:
	...
class PartyNameSetErrorMessage(AbstractPartyMessage):
	def __init__(self, result:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.result=result