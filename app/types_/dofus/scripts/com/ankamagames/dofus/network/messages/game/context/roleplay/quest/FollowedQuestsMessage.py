from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.quest.QuestActiveDetailedInformations import QuestActiveDetailedInformations
class FollowedQuestsMessage:
	def __init__(self, quests:list[QuestActiveDetailedInformations]):
		self.quests=quests