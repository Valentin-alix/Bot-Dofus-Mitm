from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect
class AlterationInfo:
	def __init__(self, alterationId:int, creationTime:float, expirationType:int, expirationValue:float, effects:list[ObjectEffect]):
		self.alterationId=alterationId
		self.creationTime=creationTime
		self.expirationType=expirationType
		self.expirationValue=expirationValue
		self.effects=effects