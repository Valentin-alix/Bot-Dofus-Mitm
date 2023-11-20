from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.collector.tax.TaxCollectorBasicInformations import TaxCollectorBasicInformations
class TaxCollectorMovement:
	def __init__(self, movementType:int, basicInfos:TaxCollectorBasicInformations, playerId:int, playerName:str):
		self.movementType=movementType
		self.basicInfos=basicInfos
		self.playerId=playerId
		self.playerName=playerName