from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.atlas.compass.CompassUpdateMessage import CompassUpdateMessage
if TYPE_CHECKING:
	...
class CompassUpdatePartyMemberMessage(CompassUpdateMessage):
	def __init__(self, memberId:int, active:bool, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.memberId=memberId
		self.active=active