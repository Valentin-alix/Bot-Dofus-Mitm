from com.ankamagames.dofus.datacenter.effects.EffectInstance import EffectInstance
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter


class EffectInstanceCreature(EffectInstance):

    monsterFamilyId: int

    def __init__(self):
        super().__init__()

    def clone(self) -> EffectInstance:
        o: EffectInstanceCreature = EffectInstanceCreature()
        o.rawZone = self.rawZone
        o.effectId = self.effectId
        o.duration = self.duration
        o.delay = self.delay
        o.monsterFamilyId = self.monsterFamilyId
        o.random = self.random
        o.group = self.group
        o.targetId = self.targetId
        o.targetMask = self.targetMask
        return o

    @property
    def parameter0(self) -> object:
        return self.monsterFamilyId

    def setParameter(self, paramIndex: int, value) -> None:
        if paramIndex == 0:
            self.monsterFamilyId = int(value)
