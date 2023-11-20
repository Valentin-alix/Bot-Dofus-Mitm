from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.friend.AcquaintanceInformation import AcquaintanceInformation
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus
class AcquaintanceOnlineInformation(AcquaintanceInformation):
	def __init__(self, playerId:int, playerName:str, moodSmileyId:int, status:PlayerStatus, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.playerId=playerId
		self.playerName=playerName
		self.moodSmileyId=moodSmileyId
		self.status=status