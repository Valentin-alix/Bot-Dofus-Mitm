from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterInformations import GameFightFighterInformations
if TYPE_CHECKING:
	...
class GameFightAIInformations(GameFightFighterInformations):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		...