from com.ankamagames.dofus.datacenter.effects.EffectInstance import EffectInstance
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter


class EffectInstanceDuration(EffectInstance, IDataCenter):

    days: int

    hours: int

    minutes: int

    def __init__(self):
        super().__init__()

    def clone(self) -> "EffectInstance":
        o: EffectInstanceDuration = EffectInstanceDuration()
        o.rawZone = self.rawZone
        o.effectId = self.ffectId
        o.duration = self.duration
        o.delay = self.delay
        o.days = self.days
        o.hours = self.hours
        o.minutes = self.minutes
        o.random = self.random
        o.group = self.group
        o.targetId = self.targetId
        o.targetMask = self.targetMask
        return o

    @property
    def parameter0(self) -> object:
        return self.days

    @property
    def parameter1(self) -> object:
        return self.hours

    @property
    def parameter2(self) -> object:
        return self.minutes

    def setParameter(self, paramIndex: int, value) -> None:
        if paramIndex == 0:
            self.days = int(value)
        elif paramIndex == 1:
            self.hours = int(value)
        elif paramIndex == 2:
            self.minutes = int(value)
