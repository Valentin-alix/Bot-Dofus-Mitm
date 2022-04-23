from com.ankamagames.dofus.datacenter.effects.EffectInstance import EffectInstance
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter


class EffectInstanceMinMax(EffectInstance, IDataCenter):

    min: int

    max: int

    def __init__(self):
        super().__init__()

    def clone(self) -> EffectInstance:
        o: EffectInstanceMinMax = EffectInstanceMinMax()
        o.rawZone = self.rawZone
        o.effectId = self.effectId
        o.duration = self.duration
        o.delay = self.delay
        o.min = self.min
        o.max = self.max
        o.random = self.random
        o.group = self.group
        o.targetId = self.targetId
        o.targetMask = self.targetMask
        return o

    @property
    def parameter0(self) -> object:
        return self.min

    @property
    def parameter1(self) -> object:
        return self.max if self.min != self.max else None

    def setParameter(self, paramIndex: int, value) -> None:
        if paramIndex == 0:
            self.min = int(value)
        elif paramIndex == 1:
            self.max = int(value)
