from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.social.SocialEmblem import SocialEmblem
class AllianceCreationValidMessage:
	def __init__(self, allianceName:str, allianceTag:str, allianceEmblem:SocialEmblem):
		self.allianceName=allianceName
		self.allianceTag=allianceTag
		self.allianceEmblem=allianceEmblem