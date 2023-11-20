from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.social.application.SocialApplicationInformation import SocialApplicationInformation
class AllianceListApplicationModifiedMessage:
	def __init__(self, apply:SocialApplicationInformation, state:int, playerId:int):
		self.apply=apply
		self.state=state
		self.playerId=playerId