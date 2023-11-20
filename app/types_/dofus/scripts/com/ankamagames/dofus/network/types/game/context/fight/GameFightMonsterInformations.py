from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.GameFightAIInformations import GameFightAIInformations
if TYPE_CHECKING:
	...
class GameFightMonsterInformations(GameFightAIInformations):
	def __init__(self, creatureGenericId:int, creatureGrade:int, creatureLevel:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.creatureGenericId=creatureGenericId
		self.creatureGrade=creatureGrade
		self.creatureLevel=creatureLevel