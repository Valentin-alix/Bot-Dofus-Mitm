from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.treasureHunt.TreasureHuntStep import TreasureHuntStep
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.treasureHunt.TreasureHuntFlag import TreasureHuntFlag
class TreasureHuntMessage:
	def __init__(self, questType:int, startMapId:float, knownStepsList:list[TreasureHuntStep], totalStepCount:int, checkPointCurrent:int, checkPointTotal:int, availableRetryCount:int, flags:list[TreasureHuntFlag]):
		self.questType=questType
		self.startMapId=startMapId
		self.knownStepsList=knownStepsList
		self.totalStepCount=totalStepCount
		self.checkPointCurrent=checkPointCurrent
		self.checkPointTotal=checkPointTotal
		self.availableRetryCount=availableRetryCount
		self.flags=flags