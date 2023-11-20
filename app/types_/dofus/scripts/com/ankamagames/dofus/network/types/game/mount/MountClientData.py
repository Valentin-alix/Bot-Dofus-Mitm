from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffectInteger import ObjectEffectInteger
class MountClientData:
	def __init__(self, id:float, model:int, ancestor:list[int], behaviors:list[int], name:str, ownerId:int, experience:int, experienceForLevel:int, experienceForNextLevel:float, level:int, maxPods:int, stamina:int, staminaMax:int, maturity:int, maturityForAdult:int, energy:int, energyMax:int, serenity:int, aggressivityMax:int, serenityMax:int, love:int, loveMax:int, fecondationTime:int, boostLimiter:int, boostMax:float, reproductionCount:int, reproductionCountMax:int, harnessGID:int, effectList:list[ObjectEffectInteger]):
		self.id=id
		self.model=model
		self.ancestor=ancestor
		self.behaviors=behaviors
		self.name=name
		self.ownerId=ownerId
		self.experience=experience
		self.experienceForLevel=experienceForLevel
		self.experienceForNextLevel=experienceForNextLevel
		self.level=level
		self.maxPods=maxPods
		self.stamina=stamina
		self.staminaMax=staminaMax
		self.maturity=maturity
		self.maturityForAdult=maturityForAdult
		self.energy=energy
		self.energyMax=energyMax
		self.serenity=serenity
		self.aggressivityMax=aggressivityMax
		self.serenityMax=serenityMax
		self.love=love
		self.loveMax=loveMax
		self.fecondationTime=fecondationTime
		self.boostLimiter=boostLimiter
		self.boostMax=boostMax
		self.reproductionCount=reproductionCount
		self.reproductionCountMax=reproductionCountMax
		self.harnessGID=harnessGID
		self.effectList=effectList