from com.ankamagames.dofus.datacenter.effects.EffectInstance import EffectInstance
from com.ankamagames.dofus.datacenter.effects.instances.EffectInstanceInteger import (
    EffectInstanceInteger,
)
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter


class EffectInstanceMount(EffectInstance):

    id: float

    expirationDate: float

    model: int

    name: str = ""

    owner: str = ""

    level: int = 0

    sex: bool = False

    isRideable: bool = False

    isFeconded: bool = False

    isFecondationReady: bool = False

    reproductionCount: int = 0

    reproductionCountMax: int = 0

    effects: list[EffectInstanceInteger]

    capacities: list[int]

    def __init__(self):
        self.effects = list[EffectInstanceInteger]()
        self.capacities = list[int]()
        super().__init__()

    def clone(self) -> EffectInstance:
        o: EffectInstanceMount = EffectInstanceMount()
        o.rawZone = self.rawZone
        o.effectId = self.effectId
        o.duration = self.duration
        o.delay = self.delay
        o.random = self.random
        o.group = self.group
        o.targetId = self.targetId
        o.targetMask = self.targetMask
        o.id = self.id
        o.expirationDate = self.expirationDate
        o.model = self.model
        o.name = self.name
        o.owner = self.owner
        o.level = self.level
        o.sex = self.sex
        o.isRideable = self.isRideable
        o.isFeconded = self.isFeconded
        o.isFecondationReady = self.isFecondationReady
        o.reproductionCount = self.reproductionCount
        o.reproductionCountMax = self.reproductionCountMax
        o.effects = self.effects
        o.capacities = self.capacities
        return o

    @property
    def parameter0(self) -> object:
        return self.id

    @property
    def parameter1(self) -> object:
        return self.expirationDate

    @property
    def parameter2(self) -> object:
        return self.model

    @property
    def parameter3(self) -> object:
        return self.name

    @property
    def parameter4(self) -> object:
        return self.owner

    def setParameter(self, paramIndex: int, value) -> None:
        if paramIndex == 0:
            self.id = float(value)
        elif paramIndex == 1:
            self.expirationDate = float(value)
        elif paramIndex == 2:
            self.model = int(value)
        elif paramIndex == 3:
            self.name = str(value)
        elif paramIndex == 4:
            self.owner = str(value)
