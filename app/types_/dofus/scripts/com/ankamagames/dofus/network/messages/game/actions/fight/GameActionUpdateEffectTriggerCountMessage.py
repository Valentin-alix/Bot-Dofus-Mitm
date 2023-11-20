from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.GameFightEffectTriggerCount import GameFightEffectTriggerCount
class GameActionUpdateEffectTriggerCountMessage:
	def __init__(self, targetIds:list[GameFightEffectTriggerCount]):
		self.targetIds=targetIds