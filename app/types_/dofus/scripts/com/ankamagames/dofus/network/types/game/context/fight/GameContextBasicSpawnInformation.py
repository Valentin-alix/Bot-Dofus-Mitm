from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.GameContextActorPositionInformations import GameContextActorPositionInformations
class GameContextBasicSpawnInformation:
	def __init__(self, teamId:int, alive:bool, informations:GameContextActorPositionInformations):
		self.teamId=teamId
		self.alive=alive
		self.informations=informations