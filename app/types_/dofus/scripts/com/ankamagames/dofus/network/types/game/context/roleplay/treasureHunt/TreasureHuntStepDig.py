from __future__ import annotations
from typing import TYPE_CHECKING
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.roleplay.treasureHunt.TreasureHuntStep import TreasureHuntStep
if TYPE_CHECKING:
	...
class TreasureHuntStepDig(TreasureHuntStep):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		...