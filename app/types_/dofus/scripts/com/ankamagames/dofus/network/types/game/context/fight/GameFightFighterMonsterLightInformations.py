from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterLightInformations import GameFightFighterLightInformations
if TYPE_CHECKING:
	...
class GameFightFighterMonsterLightInformations(GameFightFighterLightInformations):
	def __init__(self, creatureGenericId:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.creatureGenericId=creatureGenericId