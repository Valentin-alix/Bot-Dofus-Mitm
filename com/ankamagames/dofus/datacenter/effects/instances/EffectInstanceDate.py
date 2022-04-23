from com.ankamagames.dofus.datacenter.effects.EffectInstance import EffectInstance
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter


class EffectInstanceDate(EffectInstance):

    year: int

    month: int

    day: int

    hour: int

    minute: int

    def __init__(self):
        super().__init__()

    def clone(self) -> EffectInstance:
        o: EffectInstanceDate = EffectInstanceDate()
        o.rawZone = self.rawZone
        o.effectId = self.effectId
        o.duration = self.duration
        o.delay = self.delay
        o.year = self.year
        o.month = self.month
        o.day = self.day
        o.hour = self.hour
        o.minute = self.minute
        o.random = self.random
        o.group = self.group
        o.targetId = self.targetId
        o.targetMask = self.targetMask
        return o

    @property
    def parameter0(self) -> object:
        return str(self.year)

    @property
    def parameter1(self) -> object:
        smonth: str = str(self.month) if self.month > 9 else "0" + str(self.month)
        sday: str = str(self.day) if self.day > 9 else "0" + str(self.day)
        return smonth + sday

    @property
    def parameter2(self) -> object:
        shour: str = str(self.hour) if self.hour > 9 else "0" + str(self.hour)
        sminute: str = str(self.minute) if self.minute > 9 else "0" + str(self.minute)
        return shour + sminute

    @property
    def parameter3(self) -> object:
        return self.month

    @property
    def parameter4(self) -> object:
        return self.day

    def setParameter(self, paramIndex: int, value) -> None:
        if paramIndex == 0:
            self.year = int(value)
        elif paramIndex == 1:
            self.month = int(str(value).substr(0, 2))
            self.day = int(str(value).substr(2, 2))
        elif paramIndex == 2:
            self.hour = int(str(value).substr(0, 2))
            self.minute = int(str(value).substr(2, 2))
        elif paramIndex == 3:
            self.month = int(value)
        elif paramIndex == 4:
            self.day = int(value)
