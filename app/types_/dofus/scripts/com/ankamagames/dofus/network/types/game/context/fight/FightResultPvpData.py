from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.FightResultAdditionalData import FightResultAdditionalData
if TYPE_CHECKING:
	...
class FightResultPvpData(FightResultAdditionalData):
	def __init__(self, grade:int, minHonorForGrade:int, maxHonorForGrade:int, honor:int, honorDelta:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.grade=grade
		self.minHonorForGrade=minHonorForGrade
		self.maxHonorForGrade=maxHonorForGrade
		self.honor=honor
		self.honorDelta=honorDelta