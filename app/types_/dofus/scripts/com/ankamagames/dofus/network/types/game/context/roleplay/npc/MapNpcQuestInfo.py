from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.quest.GameRolePlayNpcQuestFlag import GameRolePlayNpcQuestFlag
class MapNpcQuestInfo:
	def __init__(self, mapId:float, npcsIdsWithQuest:list[int], questFlags:list[GameRolePlayNpcQuestFlag]):
		self.mapId=mapId
		self.npcsIdsWithQuest=npcsIdsWithQuest
		self.questFlags=questFlags