from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.alliance.application.AlliancePlayerApplicationAbstractMessage import AlliancePlayerApplicationAbstractMessage
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.AllianceInformation import AllianceInformation
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.social.application.SocialApplicationInformation import SocialApplicationInformation
class AlliancePlayerApplicationInformationMessage(AlliancePlayerApplicationAbstractMessage):
	def __init__(self, allianceInformation:AllianceInformation, apply:SocialApplicationInformation, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.allianceInformation=allianceInformation
		self.apply=apply