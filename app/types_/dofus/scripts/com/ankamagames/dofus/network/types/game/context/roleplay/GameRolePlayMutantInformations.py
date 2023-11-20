from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayHumanoidInformations import GameRolePlayHumanoidInformations
if TYPE_CHECKING:
	...
class GameRolePlayMutantInformations(GameRolePlayHumanoidInformations):
	def __init__(self, monsterId:int, powerLevel:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.monsterId=monsterId
		self.powerLevel=powerLevel