from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterLightInformations import GameFightFighterLightInformations
if TYPE_CHECKING:
	...
class GameFightFighterEntityLightInformation(GameFightFighterLightInformations):
	def __init__(self, entityModelId:int, masterId:float, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.entityModelId=entityModelId
		self.masterId=masterId