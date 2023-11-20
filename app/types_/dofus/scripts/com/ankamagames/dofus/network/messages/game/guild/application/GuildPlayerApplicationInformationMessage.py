from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.guild.application.GuildPlayerApplicationAbstractMessage import GuildPlayerApplicationAbstractMessage
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.social.application.SocialApplicationInformation import SocialApplicationInformation
class GuildPlayerApplicationInformationMessage(GuildPlayerApplicationAbstractMessage):
	def __init__(self, guildInformation:GuildInformations, apply:SocialApplicationInformation, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.guildInformation=guildInformation
		self.apply=apply