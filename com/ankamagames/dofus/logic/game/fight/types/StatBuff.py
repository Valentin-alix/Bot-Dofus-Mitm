from com.ankamagames.dofus.datacenter.effects.Effect import Effect
from com.ankamagames.dofus.datacenter.effects.instances.EffectInstanceDice import (
    EffectInstanceDice,
)
import com.ankamagames.dofus.logic.game.fight.types.BasicBuff as basicBuff
from com.ankamagames.dofus.logic.game.fight.types.CastingSpell import CastingSpell
from com.ankamagames.dofus.network.types.game.actions.fight.FightTemporaryBoostEffect import (
    FightTemporaryBoostEffect,
)
from com.ankamagames.jerakine.logger.Logger import Logger

logger = Logger(__name__)


class StatBuff(basicBuff.BasicBuff):

    _statName: str

    _isABoost: bool

    isRecent: bool

    def __init__(
        self,
        effect: FightTemporaryBoostEffect = None,
        castingSpell: CastingSpell = None,
        actionId: int = 0,
        isRecent: bool = False,
    ):
        if effect:
            super().__init__(effect, castingSpell, actionId, effect.delta, None, None)
            self._statName = ActionIdHelper.getActionIdStatName(actionId)
            self._isABoost = ActionIdHelper.isBuff(actionId)
            self.isRecent = isRecent

    @property
    def type(self) -> str:
        return "StatBuff"

    @property
    def statName(self) -> str:
        return self._statName

    @property
    def delta(self) -> int:
        if isinstance(self._effect, EffectInstanceDice):
            return self._effect.diceNum if self._isABoost else -self._effect.diceNum
        return 0

    def onReenable(self) -> None:
        super().onReenable()
        effect: Effect = Effect.getEffectById(self.actionId)
        if effect is not None and effect.active:
            self.onApplied()

    def clone(self, id: int = 0) -> basicBuff.BasicBuff:
        sb: StatBuff = StatBuff()
        sb._statName = self._statName
        sb._isABoost = self._isABoost
        sb.id = self.uid
        sb.uid = self.uid
        sb.dataUid = self.dataUid
        sb.actionId = self.actionId
        sb.targetId = self.targetId
        sb.castingSpell = self.castingSpell
        sb.duration = self.duration
        sb.dispelable = self.dispelable
        sb.source = self.source
        sb.aliveSource = self.aliveSource
        sb.sourceJustReaffected = self.sourceJustReaffected
        sb.parentBoostUid = self.parentBoostUid
        sb.initParam(self.param1, self.param2, self.param3)
        return sb
