from com.ankamagames.dofus.datacenter.spells.Spell import Spell
from com.ankamagames.dofus.datacenter.spells.SpellLevel import SpellLevel
from com.ankamagames.jerakine.types.positions.MapPoint import MapPoint


class CastingSpell:

    _unicID: int = 0

    castingSpellId: int

    casterId: float

    targetedCell: MapPoint

    spell: Spell

    spellRank: SpellLevel

    markId: int

    markType: int

    silentCast: bool

    weaponId: int = -1

    isCriticalHit: bool

    isCriticalFail: bool

    portalIds: list[int]

    portalMapPoints: list[MapPoint]

    defaultTargetGfxId: int

    def __init__(self, updateCastingId: bool = True):
        if updateCastingId:
            self.castingSpellId = self._unicID
            self._unicID += 1
