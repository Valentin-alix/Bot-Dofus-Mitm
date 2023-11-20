from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.action.fight.FightDispellableEffectExtendedInformations import FightDispellableEffectExtendedInformations
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.actions.fight.GameActionMark import GameActionMark
	from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.context.fight.GameFightEffectTriggerCount import GameFightEffectTriggerCount
class GameFightSpectateMessage:
	def __init__(self, effects:list[FightDispellableEffectExtendedInformations], marks:list[GameActionMark], gameTurn:int, fightStart:int, fxTriggerCounts:list[GameFightEffectTriggerCount]):
		self.effects=effects
		self.marks=marks
		self.gameTurn=gameTurn
		self.fightStart=fightStart
		self.fxTriggerCounts=fxTriggerCounts