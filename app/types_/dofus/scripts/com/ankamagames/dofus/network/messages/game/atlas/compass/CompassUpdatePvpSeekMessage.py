from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.atlas.compass.CompassUpdateMessage import CompassUpdateMessage
if TYPE_CHECKING:
	...
class CompassUpdatePvpSeekMessage(CompassUpdateMessage):
	def __init__(self, memberId:int, memberName:str, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.memberId=memberId
		self.memberName=memberName