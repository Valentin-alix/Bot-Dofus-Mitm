from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.character.restriction.ActorRestrictionsInformations import ActorRestrictionsInformations
class SetCharacterRestrictionsMessage:
	def __init__(self, actorId:float, restrictions:ActorRestrictionsInformations):
		self.actorId=actorId
		self.restrictions=restrictions