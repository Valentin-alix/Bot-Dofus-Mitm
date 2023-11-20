from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.social.SocialNoticeSetRequestMessage import SocialNoticeSetRequestMessage
if TYPE_CHECKING:
	...
class GuildMotdSetRequestMessage(SocialNoticeSetRequestMessage):
	def __init__(self, content:str, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.content=content