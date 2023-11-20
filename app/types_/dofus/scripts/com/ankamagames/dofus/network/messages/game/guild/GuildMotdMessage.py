from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.social.SocialNoticeMessage import SocialNoticeMessage
if TYPE_CHECKING:
	...
class GuildMotdMessage(SocialNoticeMessage):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		...