from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
class ContactLookMessage:
	def __init__(self, requestId:int, playerName:str, playerId:int, look:EntityLook):
		self.requestId=requestId
		self.playerName=playerName
		self.playerId=playerId
		self.look=look