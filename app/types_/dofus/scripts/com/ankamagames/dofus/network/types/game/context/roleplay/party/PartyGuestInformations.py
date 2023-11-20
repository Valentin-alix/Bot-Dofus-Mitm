from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.party.entity.PartyEntityBaseInformation import PartyEntityBaseInformation
class PartyGuestInformations:
	def __init__(self, guestId:int, hostId:int, name:str, guestLook:EntityLook, breed:int, sex:bool, status:PlayerStatus, entities:list[PartyEntityBaseInformation]):
		self.guestId=guestId
		self.hostId=hostId
		self.name=name
		self.guestLook=guestLook
		self.breed=breed
		self.sex=sex
		self.status=status
		self.entities=entities