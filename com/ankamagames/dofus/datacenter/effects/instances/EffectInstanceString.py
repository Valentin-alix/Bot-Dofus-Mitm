from com.ankamagames.dofus.datacenter.effects.EffectInstance import EffectInstance
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter


class EffectInstanceString(EffectInstance):

    text: str

    def __init__(self):
        super().__init__()

    def clone(self) -> EffectInstance:
        o: EffectInstanceString = EffectInstanceString()
        o.rawZone = self.rawZone
        o.effectId = self.effectId
        o.duration = self.duration
        o.delay = self.delay
        o.text = self.text
        o.random = self.random
        o.group = self.group
        o.targetId = self.targetId
        o.targetMask = self.targetMask
        return o

    @property
    def parameter3(self) -> object:
        return self.text

    def setParameter(self, paramIndex: int, value) -> None:
        if paramIndex == 3:
            self.text = str(value)
