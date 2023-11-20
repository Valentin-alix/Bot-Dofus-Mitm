from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.BasicNamedAllianceInformations import BasicNamedAllianceInformations
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.social.SocialEmblem import SocialEmblem
class AllianceInformation(BasicNamedAllianceInformations):
	def __init__(self, allianceEmblem:SocialEmblem, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.allianceEmblem=allianceEmblem