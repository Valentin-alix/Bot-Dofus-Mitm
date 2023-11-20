from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayActorInformations import GameRolePlayActorInformations
if TYPE_CHECKING:
	...
class GameRolePlayTreasureHintInformations(GameRolePlayActorInformations):
	def __init__(self, npcId:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.npcId=npcId