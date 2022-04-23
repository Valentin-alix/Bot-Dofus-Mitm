from com.ankamagames.dofus.datacenter.effects.EffectInstance import EffectInstance


class EffectZone:

    _effect: EffectInstance = EffectInstance()

    zoneSize: object

    zoneShape: int

    zoneMinSize: object

    zoneEfficiencyPercent: object

    zoneMaxEfficiency: object

    zoneStopAtTarget: object

    _targetMask: str

    def __init__(self, rawZone: str, targetMask: str):
        super().__init__()
        self._effect.rawZone = rawZone
        self.zoneSize = self._effect.zoneSize
        self.zoneShape = self._effect.zoneShape
        self.zoneMinSize = self._effect.zoneMinSize
        self.zoneEfficiencyPercent = self._effect.zoneEfficiencyPercent
        self.zoneMaxEfficiency = self._effect.zoneMaxEfficiency
        self.zoneStopAtTarget = self._effect.zoneStopAtTarget
        self._targetMask = targetMask

    @property
    def targetMask(self) -> str:
        return self._targetMask
