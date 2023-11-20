from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterNamedInformations import GameFightFighterNamedInformations
if TYPE_CHECKING:
	...
class GameFightMutantInformations(GameFightFighterNamedInformations):
	def __init__(self, powerLevel:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.powerLevel=powerLevel