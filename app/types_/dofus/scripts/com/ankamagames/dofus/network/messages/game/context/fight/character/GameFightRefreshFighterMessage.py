from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.GameContextActorInformations import GameContextActorInformations
class GameFightRefreshFighterMessage:
	def __init__(self, informations:GameContextActorInformations):
		self.informations=informations