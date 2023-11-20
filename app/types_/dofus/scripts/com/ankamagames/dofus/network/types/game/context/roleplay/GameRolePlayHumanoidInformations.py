from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayNamedActorInformations import GameRolePlayNamedActorInformations
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.HumanInformations import HumanInformations
class GameRolePlayHumanoidInformations(GameRolePlayNamedActorInformations):
	def __init__(self, humanoidInfo:HumanInformations, accountId:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.humanoidInfo=humanoidInfo
		self.accountId=accountId