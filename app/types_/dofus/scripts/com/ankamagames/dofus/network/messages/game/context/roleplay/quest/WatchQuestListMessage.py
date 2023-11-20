from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.messages.game.context.roleplay.quest.QuestListMessage import QuestListMessage
if TYPE_CHECKING:
	...
class WatchQuestListMessage(QuestListMessage):
	def __init__(self, playerId:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.playerId=playerId