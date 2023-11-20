from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterLightInformations import GameFightFighterLightInformations
if TYPE_CHECKING:
	...
class GameFightFighterNamedLightInformations(GameFightFighterLightInformations):
	def __init__(self, name:str, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.name=name