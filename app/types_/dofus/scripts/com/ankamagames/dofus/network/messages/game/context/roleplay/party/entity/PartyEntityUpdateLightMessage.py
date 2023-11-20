from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyUpdateLightMessage import PartyUpdateLightMessage
if TYPE_CHECKING:
	...
class PartyEntityUpdateLightMessage(PartyUpdateLightMessage):
	def __init__(self, indexId:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.indexId=indexId