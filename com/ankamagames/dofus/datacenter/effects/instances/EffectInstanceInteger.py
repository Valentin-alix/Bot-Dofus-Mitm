from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from com.ankamagames.dofus.datacenter.effects.instances.EffectInstanceDice import (
        EffectInstanceDice,
    )
import com.ankamagames.dofus.datacenter.effects.EffectInstance as effinst
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter
from com.ankamagames.jerakine.logger.Logger import Logger

logger = Logger(__name__)


class EffectInstanceInteger(effinst.EffectInstance, IDataCenter):

    value: int

    def __init__(self):
        super().__init__()

    def clone(self) -> effinst.EffectInstance:
        o: EffectInstanceInteger = EffectInstanceInteger()
        o.rawZone = self.rawZone
        o.effectId = self.effectId
        o.order = self.order
        o.duration = self.duration
        o.delay = self.delay
        o.value = self.value
        o.random = self.random
        o.group = self.group
        o.visibleInTooltip = self.visibleInTooltip
        o.visibleInBuffUi = self.visibleInBuffUi
        o.visibleInFightLog = self.visibleInFightLog
        o.visibleOnTerrain = self.visibleOnTerrain
        o.targetId = self.targetId
        o.targetMask = self.targetMask
        o.forClientOnly = self.forClientOnly
        o.dispellable = self.dispellable
        return o

    @property
    def parameter0(self) -> object:
        return self.value

    def setParameter(self, paramIndex: int, value) -> None:
        if paramIndex == 2:
            self.value = int(value)

    def add(self, term) -> effinst.EffectInstance:
        if isinstance(term, EffectInstanceDice):
            return term.add(self)
        if isinstance(term, EffectInstanceInteger):
            self.value += term.value
            self.forceDescriptionRefresh()
        else:
            logger.error(term + " cannot be added to EffectInstanceInteger.")
        return self
