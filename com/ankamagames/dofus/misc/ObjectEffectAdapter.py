from com.ankamagames.dofus.datacenter.effects.instances.EffectInstanceString import (
    EffectInstanceString,
)
from com.ankamagames.dofus.enums.ActionIds import ActionIds
from com.ankamagames.dofus.datacenter.effects.EffectInstance import EffectInstance
from com.ankamagames.dofus.datacenter.effects.instances.EffectInstanceCreature import (
    EffectInstanceCreature,
)
from com.ankamagames.dofus.datacenter.effects.instances.EffectInstanceDate import (
    EffectInstanceDate,
)
from com.ankamagames.dofus.datacenter.effects.instances.EffectInstanceDice import (
    EffectInstanceDice,
)
from com.ankamagames.dofus.datacenter.effects.instances.EffectInstanceDuration import (
    EffectInstanceDuration,
)
from com.ankamagames.dofus.datacenter.effects.instances.EffectInstanceInteger import (
    EffectInstanceInteger,
)
from com.ankamagames.dofus.datacenter.effects.instances.EffectInstanceLadder import (
    EffectInstanceLadder,
)
from com.ankamagames.dofus.datacenter.effects.instances.EffectInstanceMinMax import (
    EffectInstanceMinMax,
)
from com.ankamagames.dofus.datacenter.effects.instances.EffectInstanceMount import (
    EffectInstanceMount,
)
from com.ankamagames.dofus.datacenter.items.IncarnationLevel import IncarnationLevel
from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import (
    ObjectEffect,
)
from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffectCreature import (
    ObjectEffectCreature,
)
from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffectDate import (
    ObjectEffectDate,
)
from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffectDice import (
    ObjectEffectDice,
)
from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffectDuration import (
    ObjectEffectDuration,
)
from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffectInteger import (
    ObjectEffectInteger,
)
from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffectLadder import (
    ObjectEffectLadder,
)
from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffectMinMax import (
    ObjectEffectMinMax,
)
from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffectMount import (
    ObjectEffectMount,
)
from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffectString import (
    ObjectEffectString,
)
from com.ankamagames.jerakine.logger.Logger import Logger

logger = Logger(__name__)


class ObjectEffectAdapter:
    def fromNetwork(self, oe: ObjectEffect) -> EffectInstance:
        effect: EffectInstance = None
        level: int = 0
        floor: int = 0
        nextFloor: int = 0
        incLevel: IncarnationLevel = None
        incLevelPlusOne: IncarnationLevel = None
        serverEffect: ObjectEffectInteger = None
        clientEffects: list[EffectInstanceInteger] = None
        intEffect: EffectInstanceInteger = None
        if oe is ObjectEffectDice and oe.actionId == ActionIds.ACTION_INCARNATION:
            effect = EffectInstanceDate()
            effect.year = ObjectEffectDice(oe).diceNum
            effect.month = (
                ObjectEffectDice(oe).diceSide * 32768 + ObjectEffectDice(oe).diceConst
            )
            level = 1
            while True:
                incLevel = IncarnationLevel.getIncarnationLevelByIdAndLevel(
                    ObjectEffectDice(oe).diceNum, level
                )
                if incLevel:
                    floor = incLevel.requiredXp
                level += 1
                incLevelPlusOne = IncarnationLevel.getIncarnationLevelByIdAndLevel(
                    ObjectEffectDice(oe).diceNum, level
                )
                if incLevelPlusOne:
                    nextFloor = incLevelPlusOne.requiredXp
                if nextFloor < effect.month and level < 51:
                    break
            level -= 1
            effect.day = level
            effect.hour = 0
            effect.minute = 0
        else:
            if isinstance(oe, ObjectEffectString):
                effect = EffectInstanceString()
                effect.text = ObjectEffectString(oe).value
            elif isinstance(oe, ObjectEffectInteger):
                effect = EffectInstanceInteger()
                EffectInstanceInteger(effect).value = ObjectEffectInteger(oe).value
            elif isinstance(oe, ObjectEffectMinMax):
                effect = EffectInstanceMinMax()
                effect.min = ObjectEffectMinMax(oe).min
                effect.max = ObjectEffectMinMax(oe).max
            elif isinstance(oe, ObjectEffectDice):
                effect = EffectInstanceDice()
                EffectInstanceDice(effect).diceNum = ObjectEffectDice(oe).diceNum
                EffectInstanceDice(effect).diceSide = ObjectEffectDice(oe).diceSide
                EffectInstanceDice(effect).value = ObjectEffectDice(oe).diceConst
            elif isinstance(oe, ObjectEffectDate):
                effect = EffectInstanceDate()
                effect.year = ObjectEffectDate(oe).year
                effect.month = ObjectEffectDate(oe).month + 1
                effect.day = ObjectEffectDate(oe).day
                effect.hour = ObjectEffectDate(oe).hour
                effect.minute = ObjectEffectDate(oe).minute
            elif isinstance(oe, ObjectEffectDuration):
                effect = EffectInstanceDuration()
                effect.days = ObjectEffectDuration(oe).days
                effect.hours = ObjectEffectDuration(oe).hours
                effect.minutes = ObjectEffectDuration(oe).minutes
            elif isinstance(oe, ObjectEffectLadder):
                effect = EffectInstanceLadder()
                effect.monsterFamilyId = ObjectEffectLadder(oe).monsterFamilyId
                effect.monsterCount = ObjectEffectLadder(oe).monsterCount
            elif isinstance(oe, ObjectEffectCreature):
                effect = EffectInstanceCreature()
                effect.monsterFamilyId = ObjectEffectCreature(oe).monsterFamilyId
            elif isinstance(oe, ObjectEffectMount):
                effect = EffectInstanceMount()
                effect.id = oe.id
                effect.expirationDate = oe.expirationDate
                effect.model = oe.model
                effect.owner = oe.owner
                effect.name = oe.name
                effect.level = oe.level
                effect.sex = oe.sex
                effect.isRideable = oe.isRideable
                effect.isFecondationReady = oe.isFecondationReady
                effect.isFeconded = oe.isFeconded
                effect.reproductionCount = oe.reproductionCount
                effect.reproductionCountMax = oe.reproductionCountMax
                clientEffects = list[EffectInstanceInteger]()
                for serverEffect in oe.effects:
                    intEffect = EffectInstanceInteger()
                    intEffect.value = serverEffect.value
                    intEffect.effectId = serverEffect.actionId
                    intEffect.duration = 0
                    clientEffects.append(intEffect)
                effect.effects = clientEffects
                effect.capacities = oe.capacities
            else:
                effect = EffectInstance()
        effect.effectId = oe.actionId
        effect.duration = 0
        return effect
