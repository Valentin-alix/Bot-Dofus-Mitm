from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayNpcInformations import GameRolePlayNpcInformations
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.quest.GameRolePlayNpcQuestFlag import GameRolePlayNpcQuestFlag
class GameRolePlayNpcWithQuestInformations(GameRolePlayNpcInformations):
	def __init__(self, questFlag:GameRolePlayNpcQuestFlag, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.questFlag=questFlag