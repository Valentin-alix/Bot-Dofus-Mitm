from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterInformations import GameFightFighterInformations
class GameFightSynchronizeMessage:
	def __init__(self, fighters:list[GameFightFighterInformations]):
		self.fighters=fighters