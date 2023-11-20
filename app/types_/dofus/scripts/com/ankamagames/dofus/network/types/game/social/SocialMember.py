from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus
class SocialMember(CharacterMinimalInformations):
	def __init__(self, breed:int, sex:bool, connected:int, hoursSinceLastConnection:int, accountId:int, status:PlayerStatus, rankId:int, enrollmentDate:float, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.breed=breed
		self.sex=sex
		self.connected=connected
		self.hoursSinceLastConnection=hoursSinceLastConnection
		self.accountId=accountId
		self.status=status
		self.rankId=rankId
		self.enrollmentDate=enrollmentDate