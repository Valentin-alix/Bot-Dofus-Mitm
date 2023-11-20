from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.treasureHunt.TreasureHuntStep import TreasureHuntStep
if TYPE_CHECKING:
	...
class TreasureHuntStepFollowDirectionToPOI(TreasureHuntStep):
	def __init__(self, direction:int, poiLabelId:int, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.direction=direction
		self.poiLabelId=poiLabelId