from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.alliance.KohAllianceInfo import KohAllianceInfo
class KohUpdateMessage:
	def __init__(self, kohAllianceInfo:list[KohAllianceInfo], startingAvaTimestamp:int, nextTickTime:float):
		self.kohAllianceInfo=kohAllianceInfo
		self.startingAvaTimestamp=startingAvaTimestamp
		self.nextTickTime=nextTickTime