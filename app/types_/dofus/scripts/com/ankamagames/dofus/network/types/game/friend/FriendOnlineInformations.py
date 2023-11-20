from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.friend.FriendInformations import FriendInformations
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus
class FriendOnlineInformations(FriendInformations):
	def __init__(self, playerId:int, playerName:str, level:int, alignmentSide:int, breed:int, guildInfo:GuildInformations, moodSmileyId:int, status:PlayerStatus, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.playerId=playerId
		self.playerName=playerName
		self.level=level
		self.alignmentSide=alignmentSide
		self.breed=breed
		self.guildInfo=guildInfo
		self.moodSmileyId=moodSmileyId
		self.status=status