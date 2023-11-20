from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus
class PlayerStatusUpdateMessage:
	def __init__(self, accountId:int, playerId:int, status:PlayerStatus):
		self.accountId=accountId
		self.playerId=playerId
		self.status=status