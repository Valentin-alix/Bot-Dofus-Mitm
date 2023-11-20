from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.social.application.ApplicationPlayerInformation import ApplicationPlayerInformation
class SocialApplicationInformation:
	def __init__(self, playerInfo:ApplicationPlayerInformation, applyText:str, creationDate:float):
		self.playerInfo=playerInfo
		self.applyText=applyText
		self.creationDate=creationDate