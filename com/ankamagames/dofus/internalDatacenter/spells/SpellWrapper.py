from typing import Any, TYPE_CHECKING
from com.ankamagames.berilia.types.messages.managers.SlotDataHolderManager import (
    SlotDataHolderManager,
)

if TYPE_CHECKING:
    from com.ankamagames.dofus.datacenter.effects.EffectInstance import EffectInstance
    from com.ankamagames.dofus.logic.game.common.spell.SpellModifiers import (
        SpellModifiers,
    )
from com.ankamagames.dofus.datacenter.effects.instances.EffectInstanceDice import (
    EffectInstanceDice,
)
from com.ankamagames.dofus.datacenter.spells.Spell import Spell
from com.ankamagames.dofus.datacenter.spells.SpellLevel import SpellLevel
from com.ankamagames.dofus.internalDatacenter.DataEnum import DataEnum
from com.ankamagames.dofus.internalDatacenter.items.ItemWrapper import ItemWrapper
from com.ankamagames.dofus.internalDatacenter.items.WeaponWrapper import WeaponWrapper
from com.ankamagames.dofus.internalDatacenter.spells.EffectZone import EffectZone
from com.ankamagames.dofus.internalDatacenter.stats.EntityStats import EntityStats
from com.ankamagames.dofus.logic.common.managers.StatsManager import StatsManager
from com.ankamagames.dofus.logic.game.common.managers.PlayedCharacterManager import (
    PlayedCharacterManager,
)
from com.ankamagames.dofus.logic.game.common.spell.SpellModifier import SpellModifier
import com.ankamagames.dofus.logic.game.fight.managers.CurrentPlayedFighterManager as cpfm
import com.ankamagames.dofus.logic.game.fight.managers.SpellModifiersManager as spellmm
from com.ankamagames.dofus.network.enums.CharacterSpellModificationTypeEnum import (
    CharacterSpellModificationTypeEnum,
)
from com.ankamagames.jerakine.data.XmlConfig import XmlConfig
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter
from com.ankamagames.jerakine.interfaces.ISlotData import ISlotData
from com.ankamagames.jerakine.interfaces.ISlotDataHolder import ISlotDataHolder
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.utils.display.EnterFrameDispatcher import (
    EnterFrameDispatcher,
)
from com.ankamagames.jerakine.utils.display.spellZone.ICellZoneProvider import (
    ICellZoneProvider,
)
from com.ankamagames.jerakine.utils.display.spellZone.IZoneShape import IZoneShape
from damageCalculation.tools.StatIds import StatIds
from com.ankamagames.dofus.logic.game.common.managers.InventoryManager import (
    InventoryManager,
)

logger = Logger(__name__)


class SpellWrapper(ISlotData, ICellZoneProvider, IDataCenter):

    _cache: list = []

    _playersCache: dict = dict()

    _cac: "SpellWrapper"

    BASE_DAMAGE_EFFECT_IDS: list = [
        100,
        96,
        97,
        98,
        99,
        92,
        93,
        94,
        95,
        1012,
        1013,
        1014,
        1015,
        1016,
    ]

    _uri: str

    _slotDataHolderManager: SlotDataHolderManager

    _canTargetCasterOutOfZone: object

    _variantActivated: bool

    _spellLevel: SpellLevel

    _spell: Spell

    id: int = 0

    spellLevel: int = 1

    effects: list["EffectInstance"]

    criticalEffect: list["EffectInstance"]

    gfxId: int

    playerId: float

    versionNum: int

    additionalEffectsZones: list[EffectZone]

    _actualCooldown: int = 0

    def __init__(self):
        super().__init__()

    @staticmethod
    def getEntityId() -> float:
        from com.ankamagames.dofus.uiApi.PlayedCharacterApi import PlayedCharacterApi

        if PlayedCharacterApi().isInFight():
            return cpfm.CurrentPlayedFighterManager().currentFighterId
        return PlayedCharacterManager().id

    @classmethod
    def create(
        cls,
        spellID: int,
        spellLevel: int = 0,
        useCache: bool = True,
        playerId: float = 0,
        variantActivated: bool = False,
        areModifiers: bool = True,
    ) -> "SpellWrapper":
        spell: SpellWrapper = None
        if spellID == 0:
            useCache = False
        if useCache:
            if cls._cache[spellID] and not playerId:
                spell = cls._cache[spellID]
            elif cls._playersCache[playerId] and cls._playersCache[playerId][spellID]:
                spell = cls._playersCache[playerId][spellID]
        if spellID == 0 and cls._cac != None:
            spell = cls._cac
        if not spell:
            spell = SpellWrapper()
            spell.id = spellID
            if useCache:
                if playerId:
                    if not cls._playersCache[playerId]:
                        cls._playersCache[playerId] = []
                    if not cls._playersCache[playerId][spellID]:
                        cls._playersCache[playerId][spellID] = spell
                else:
                    cls._cache[spellID] = spell
            spell._slotDataHolderManager = SlotDataHolderManager(spell)
        if spellID != 0 or not cls._cac:
            if spellID == 0:
                cls._cac = spell
            spell.id = spellID
            spell.gfxId = spellID
            spell.variantActivated = variantActivated
        spell.playerId = playerId
        spellData: Spell = Spell.getSpellById(spellID)
        if not spellData:
            return None
        if spellLevel == 0:
            spell.updateSpellLevelAccordingToPlayerLevel()
        else:
            spell.spellLevel = spellLevel
            spell._spellLevel = spellData.getSpellLevel(spell.spellLevel)
        spell.setSpellEffects(areModifiers)
        return spell

    def getSpellWrapperById(
        self, spellId: int, playerID: float, forceCreate: bool = False
    ) -> "SpellWrapper":
        if forceCreate:
            return self.create(spellId)
        if playerID != 0:
            if not self._playersCache[playerID]:
                return None
            if not self._playersCache[playerID][spellId] and self._cache[spellId]:
                self._playersCache[playerID][spellId] = self._cache[spellId].clone()
            if spellId == 0:
                return self._cac
            if self._playersCache[playerID][spellId]:
                return self._playersCache[playerID][spellId]
            return None
        return self._cache[spellId]

    def refreshAllPlayerSpellHolder(self, playerId: float) -> None:
        EnterFrameDispatcher().worker.addUniqueSingleTreatment(
            SpellWrapper, self.refreshSpellHolders, [playerId]
        )

    def refreshSpellHolders(self, playerID: float) -> None:
        wrapper: SpellWrapper = None
        for wrapper in self._playersCache[playerID]:
            if wrapper:
                wrapper._slotDataHolderManager.refreshAll()
        if self._cac:
            self._cac._slotDataHolderManager.refreshAll()

    def resetAllCoolDown(self, playerId: float, accessKey: object) -> None:
        for wrapper in self._playersCache[playerId]:
            wrapper.actualCooldown = 0

    def removeAllSpellWrapperBut(self, playerId: float, accessKey: object) -> None:
        temp: list = []
        for id in self._playersCache:
            if float(id) != playerId:
                temp.append(id)
        num = len(temp)
        i = 0
        while i < num:
            del self._playersCache[temp[i]]
            i += 1

    def removeAllSpellWrapper(self) -> None:
        self._playersCache = dict()
        self._cache = []

    @property
    def actualCooldown(self) -> int:
        return (
            int(self._actualCooldown) if PlayedCharacterManager().isFighting else int(0)
        )

    @actualCooldown.setter
    def actualCooldown(self, u: int) -> None:
        self._actualCooldown = u
        self._slotDataHolderManager.refreshAll()

    @property
    def spellLevelInfos(self) -> SpellLevel:
        return self._spellLevel

    def updateSpellLevelAndEffectsAccordingToPlayerLevel(self) -> None:
        self.updateSpellLevelAccordingToPlayerLevel()
        self.setSpellEffects()

    @property
    def variantActivated(self) -> bool:
        return self._variantActivated

    @variantActivated.setter
    def variantActivated(self, value: bool) -> None:
        self._variantActivated = value

    @property
    def minimalRange(self) -> int:
        return self["minRange"]

    @property
    def maximalRange(self) -> int:
        return self.spellLevelInfos.range

    @property
    def castZoneInLine(self) -> bool:
        return self["castInLine"]

    @property
    def castZoneInDiagonal(self) -> bool:
        return self["castInDiagonal"]

    @property
    def spellZoneEffects(self) -> list[IZoneShape]:
        if InventoryManager().currentBuildId != -1:
            for build in InventoryManager().builds:
                if build.id == InventoryManager().currentBuildId:
                    break
            if self.id == 0:
                for iw in build.equipment:
                    if isinstance(iw, WeaponWrapper):
                        break
                if not isinstance(iw, WeaponWrapper) and self.spellLevelInfos:
                    return self.spellLevelInfos.spellZoneEffects
        if self.id != 0 or not PlayedCharacterManager().currentWeapon:
            if self.spellLevelInfos:
                return self.spellLevelInfos.spellZoneEffects
        return None

    @property
    def hideEffects(self) -> bool:
        if self.id == 0 and PlayedCharacterManager().currentWeapon is not None:
            return PlayedCharacterManager().currentWeapon.hideEffects
        if self.spellLevelInfos:
            return self.spellLevelInfos.hideEffects
        return False

    @property
    def info1(self) -> str:
        if self.actualCooldown == 0 or not PlayedCharacterManager().isFighting:
            return None
        if self.actualCooldown == 63:
            return "-"
        return str(self.actualCooldown)

    @property
    def startTime(self) -> int:
        return 0

    @property
    def endTime(self) -> int:
        return 0

    @endTime.setter
    def endTime(self, t: int) -> None:
        pass

    @property
    def timer(self) -> int:
        return 0

    @property
    def active(self) -> bool:
        if not PlayedCharacterManager().isFighting:
            return True
        return bool(
            cpfm.CurrentPlayedFighterManager().canCastThisSpell(
                self.spellId, self.spellLevel
            )
        )

    @property
    def spell(self) -> Spell:
        if not self._spell:
            self._spell = Spell.getSpellById(self.id)
        return self._spell

    @property
    def spellId(self) -> int:
        if self.spell:
            return self.spell.id
        return 0

    @property
    def playerCriticalRate(self) -> int:
        if self["isSpellWeapon"] and not self["isDefaultSpellWeapon"]:
            weaponCriticalHit = self.getWeaponProperty("criticalHitProbability")
            currentCriticalHitProbability = (
                float(55 - weaponCriticalHit) if weaponCriticalHit > 0 else float(0)
            )
        else:
            currentCriticalHitProbability = self.getCriticalHitProbability()
        spellModifier: SpellModifier = spellmm.SpellModifiersManager().getSpellModifier(
            self.getEntityId(),
            self.id,
            CharacterSpellModificationTypeEnum.CRITICAL_HIT_BONUS,
        )
        if spellModifier is not None:
            currentCriticalHitProbability = (
                float(currentCriticalHitProbability - spellModifier.totalValue)
                if currentCriticalHitProbability > 0
                else float(0)
            )
        if currentCriticalHitProbability is not None:
            entityId = self.getEntityId()
            stats = None
            if entityId is not None:
                stats = StatsManager().getStats(entityId)
            if stats is not None:
                totalCriticalHit = stats.getStatTotalValue(
                    StatIds.CRITICAL_HIT
                ) - stats.getStatAdditionalValue(StatIds.CRITICAL_HIT)
                criticalRate = currentCriticalHitProbability - totalCriticalHit
                if criticalRate > 55:
                    criticalRate = 55
                return criticalRate
            return currentCriticalHitProbability
        return 0

    @property
    def maximalRangeWithBoosts(self) -> int:
        rangeBonus: float = None
        entityId: float = self.getEntityId()
        stats: EntityStats = StatsManager().getStats(entityId)
        spellModifiers: "SpellModifiers" = (
            spellmm.SpellModifiersManager().getSpellModifiers(entityId, self.id)
        )
        boostableRange: bool = self.spellLevelInfos.rangeCanBeBoosted
        finalRange: float = self.maximalRange
        if spellModifiers is not None:
            if not boostableRange:
                if spellModifiers.hasModifier(
                    CharacterSpellModificationTypeEnum.RANGEABLE
                ):
                    boostableRange = True
            if spellModifiers.hasModifier(CharacterSpellModificationTypeEnum.RANGE_MAX):
                finalRange += spellModifiers.getModifierValue(
                    CharacterSpellModificationTypeEnum.RANGE_MAX
                )
        if boostableRange and stats is not None:
            rangeBonus = stats.getStatTotalValue(
                StatIds.RANGE
            ) - stats.getStatAdditionalValue(StatIds.RANGE)
            finalRange += rangeBonus
        if finalRange < self.minimalRange:
            finalRange = self.minimalRange
        return finalRange

    @property
    def canTargetCasterOutOfZone(self) -> bool:
        effect: "EffectInstance" = None
        if self._canTargetCasterOutOfZone == None:
            for effect in self.effects:
                if effect.targetMask.find("C") != -1 and effect.triggers == "I":
                    self._canTargetCasterOutOfZone = True
            if not self._canTargetCasterOutOfZone:
                for effect in self.criticalEffect:
                    if effect.targetMask.find("C") != -1 and effect.triggers == "I":
                        self._canTargetCasterOutOfZone = True
            if not self._canTargetCasterOutOfZone:
                self._canTargetCasterOutOfZone = False
        return self._canTargetCasterOutOfZone

    def getProperty(self, name) -> Any:
        if hasattr(self, name):
            return getattr(self, name)
        if InventoryManager().currentBuildId != -1:
            for build in InventoryManager().builds:
                if build.id == InventoryManager().currentBuildId:
                    break
            if self.id == 0:
                for iw in build.equipment:
                    if isinstance(iw, WeaponWrapper):
                        break
                if isinstance(iw, WeaponWrapper):
                    return self.getWeaponProperty(name, iw)
        elif self.id == 0 and PlayedCharacterManager().currentWeapon != None:
            return self.getWeaponProperty(name)
        spellModifier = None
        numberToReturn = 0
        booleanToReturn = False
        if str(name) in [
            "id",
            "nameId",
            "descriptionId",
            "typeId",
            "scriptParams",
            "scriptParamsCritical",
            "scriptId",
            "scriptIdCritical",
            "iconId",
            "spellLevels",
            "useParamCache",
            "name",
            "description",
            "variants",
            "default_zone",
        ]:
            return self.spell[name]
        elif str(name) in [
            "spellBreed",
            "needFreeCell",
            "needTakenCell",
            "minPlayerLevel",
            "maxStack",
            "globalCooldown",
        ]:
            return self.spellLevelInfos[str(name)]
        if str(name) == "criticalHitProbability":
            return self.getCriticalHitProbability()
        if str(name) == "maxCastPerTurn":
            numberToReturn = self.spellLevelInfos["maxCastPerTurn"]
            spellModifier = spellmm.SpellModifiersManager().getSpellModifier(
                SpellWrapper.getEntityId(),
                self.id,
                CharacterSpellModificationTypeEnum.MAX_CAST_PER_TURN,
            )
            if spellModifier is not None:
                numberToReturn += (
                    spellModifier.contextModifValue
                    + spellModifier.objectsAndMountBonusValue
                )
            return numberToReturn
        if str(name) == "range":
            numberToReturn = self.spellLevelInfos["range"]
            spellModifier = spellmm.SpellModifiersManager().getSpellModifier(
                SpellWrapper.getEntityId(),
                self.id,
                CharacterSpellModificationTypeEnum.RANGE_MAX,
            )
            if spellModifier is not None:
                numberToReturn += (
                    spellModifier.contextModifValue
                    + spellModifier.objectsAndMountBonusValue
                )
            return numberToReturn
        if str(name) == "minRange":
            numberToReturn = self.spellLevelInfos["minRange"]
            spellModifier = spellmm.SpellModifiersManager().getSpellModifier(
                SpellWrapper.getEntityId(),
                self.id,
                CharacterSpellModificationTypeEnum.RANGE_MIN,
            )
            if spellModifier is not None:
                numberToReturn += (
                    spellModifier.contextModifValue
                    + spellModifier.objectsAndMountBonusValue
                )
            return numberToReturn
        if str(name) == "maxCastPerTarget":
            numberToReturn = self.spellLevelInfos["maxCastPerTarget"]
            spellModifier = spellmm.SpellModifiersManager().getSpellModifier(
                SpellWrapper.getEntityId(),
                self.id,
                CharacterSpellModificationTypeEnum.MAX_CAST_PER_TARGET,
            )
            if spellModifier is not None:
                numberToReturn += (
                    spellModifier.contextModifValue
                    + spellModifier.objectsAndMountBonusValue
                )
            return numberToReturn
        if str(name) == "castInLine":
            booleanToReturn = self.spellLevelInfos["castInLine"]
            spellModifier = spellmm.SpellModifiersManager().getSpellModifier(
                SpellWrapper.getEntityId(),
                self.id,
                CharacterSpellModificationTypeEnum.CAST_LINE,
            )
            if spellModifier is not None:
                booleanToReturn = booleanToReturn and spellModifier.totalValue == 0
            return booleanToReturn
        if str(name) == "castInDiagonal":
            return self.spellLevelInfos["castInDiagonal"]
        if str(name) == "castTestLos":
            booleanToReturn = self.spellLevelInfos["castTestLos"]
            spellModifier = spellmm.SpellModifiersManager().getSpellModifier(
                SpellWrapper.getEntityId(),
                self.id,
                CharacterSpellModificationTypeEnum.LOS,
            )
            if spellModifier is not None:
                booleanToReturn = booleanToReturn and spellModifier.totalValue == 0
            return booleanToReturn
        if str(name) == "rangeCanBeBoosted":
            booleanToReturn = self.spellLevelInfos["rangeCanBeBoosted"]
            spellModifier = spellmm.SpellModifiersManager().getSpellModifier(
                SpellWrapper.getEntityId(),
                self.id,
                CharacterSpellModificationTypeEnum.RANGEABLE,
            )
            if spellModifier is not None:
                booleanToReturn = booleanToReturn or spellModifier.totalValue > 0
            return booleanToReturn
        if str(name) == "apCost":
            numberToReturn = self.spellLevelInfos["apCost"]
            spellModifier = spellmm.SpellModifiersManager().getSpellModifier(
                SpellWrapper.getEntityId(),
                self.id,
                CharacterSpellModificationTypeEnum.AP_COST,
            )
            if spellModifier is not None:
                numberToReturn += -(
                    spellModifier.contextModifValue
                    + spellModifier.objectsAndMountBonusValue
                    + spellModifier.baseValue
                    + spellModifier.additionalValue
                    + spellModifier.alignGiftBonusValue
                )
            return numberToReturn
        if str(name) == "minCastInterval":
            numberToReturn = self.spellLevelInfos["minCastInterval"]
            spellModifier = spellmm.SpellModifiersManager().getSpellModifier(
                SpellWrapper.getEntityId(),
                self.id,
                CharacterSpellModificationTypeEnum.CAST_INTERVAL,
            )
            if spellModifier is not None:
                numberToReturn += -(
                    spellModifier.contextModifValue
                    + spellModifier.objectsAndMountBonusValue
                    + spellModifier.baseValue
                    + spellModifier.additionalValue
                    + spellModifier.alignGiftBonusValue
                )
            return numberToReturn
        if str(name) == "isSpellWeapon":
            return self.id == 0
        if str(name) == "isDefaultSpellWeapon":
            return self.id == 0 and not PlayedCharacterManager().currentWeapon
        if str(name) == "statesRequired":
            return self.spellLevelInfos.statesRequired
        if str(name) == "statesForbidden":
            return self.spellLevelInfos.statesForbidden
        else:
            return

    def getWeaponProperty(self, name, item: ItemWrapper = None) -> Any:
        weapon: ItemWrapper = item if item else PlayedCharacterManager().currentWeapon
        if not weapon:
            return None

        if str(name) == "id":
            return 0
        elif str(name) in [
            "nameId",
            "descriptionId",
            "iconId",
            "name",
            "description",
            "criticalHitProbability",
            "castInLine",
            "castInDiagonal",
            "castTestLos",
            "apCost",
            "minRange",
            "range",
        ]:
            return weapon[name]
        if str(name) in [
            "isDefaultSpellWeapon",
            "useParamCache",
            "needTakenCell",
            "rangeCanBeBoosted",
        ]:
            return False
        if str(name) in ["isSpellWeapon", "needFreeCell"]:
            return True
        if str(name) in [
            "minCastInterval",
            "minPlayerLevel",
            "maxStack",
            "maxCastPerTurn",
            "maxCastPerTarget",
        ]:
            return 0
        if str(name) == "typeId":
            return DataEnum.SPELL_TYPE_SPECIALS
        if str(name) in ["scriptParams", "scriptParamsCritical", "spellLevels"]:
            return None
        if str(name) in ["scriptId", "scriptIdCritical", "spellBreed"]:
            return 0
        if str(name) == "variants":
            return []
        else:
            return

    def getCriticalHitProbability(self) -> float:
        criticalHitProbability: float = self.spellLevelInfos["criticalHitProbability"]
        return (
            float(55 - criticalHitProbability) if criticalHitProbability > 0 else None
        )

    def clone(self) -> Any:
        return SpellWrapper.create(
            self.id, self.spellLevel, False, self.playerId, self.variantActivated
        )

    def addHolder(self, h: ISlotDataHolder) -> None:
        self._slotDataHolderManager.addHolder(h)

    def setLinkedSlotData(self, slotData: ISlotData) -> None:
        self._slotDataHolderManager.setLinkedSlotData(slotData)

    def removeHolder(self, h: ISlotDataHolder) -> None:
        self._slotDataHolderManager.removeHolder(h)

    def __str__(self) -> str:
        return "[SpellWrapper #" + self.id + "]"

    def updateSpellLevelAccordingToPlayerLevel(self) -> None:
        i: int = 0
        currentCharacterLevel: int = PlayedCharacterManager().limitedLevel
        if not self.spell:
            return
        spellLevels: list = self._spell.spellLevelsInfo
        spellLevelsCount: int = len(spellLevels)
        index: int = 0
        for i in range(spellLevelsCount - 1, -1, -1):
            if currentCharacterLevel >= spellLevels[i].minPlayerLevel:
                index = i
                break
        self._spellLevel = spellLevels[index]
        self.spellLevel = index + 1

    def setSpellEffects(self, areModifiers: bool = True) -> None:
        effectInstance: "EffectInstance" = None
        damageBaseSpellModifier: SpellModifier = None
        damageSpellModifier: SpellModifier = None
        healSpellModifier: SpellModifier = None
        modif: int = 0
        len: int = 0
        entityId: float = None
        effectInstanceDice: EffectInstanceDice = None
        self.effects = list["EffectInstance"]()
        self.criticalEffect = list["EffectInstance"]()
        for effectInstance in self._spellLevel.effects:
            effectInstance = effectInstance.clone()
            entityId = SpellWrapper.getEntityId()
            if areModifiers and (
                effectInstance.category == DataEnum.ACTION_TYPE_DAMAGES
                and SpellWrapper.BASE_DAMAGE_EFFECT_IDS.find(effectInstance.effectId)
                != -1
            ):
                damageBaseSpellModifier = (
                    spellmm.SpellModifiersManager().getSpellModifier(
                        entityId,
                        self.id,
                        CharacterSpellModificationTypeEnum.BASE_DAMAGE,
                    )
                )
                if damageBaseSpellModifier and effectInstance is EffectInstanceDice:
                    modif = (
                        damageBaseSpellModifier.totalValue
                        - damageBaseSpellModifier.additionalValue
                    )
                    effectInstance.diceNum += modif
                    if effectInstance.diceSide > 0:
                        effectInstance.diceSide += modif
                damageSpellModifier = spellmm.SpellModifiersManager().getSpellModifier(
                    entityId, self.id, CharacterSpellModificationTypeEnum.DAMAGE
                )
                healSpellModifier = spellmm.SpellModifiersManager().getSpellModifier(
                    entityId, self.id, CharacterSpellModificationTypeEnum.HEAL_BONUS
                )
                if damageSpellModifier:
                    effectInstance.modificator = (
                        damageSpellModifier.totalValue
                        - damageSpellModifier.additionalValue
                    )
                elif healSpellModifier:
                    effectInstance.modificator = (
                        healSpellModifier.totalValue - healSpellModifier.additionalValue
                    )
            self.effects.append(effectInstance)
        for effectInstance in self._spellLevel.criticalEffect:
            effectInstance = effectInstance.clone()
            if areModifiers and (
                effectInstance.category == DataEnum.ACTION_TYPE_DAMAGES
                and SpellWrapper.BASE_DAMAGE_EFFECT_IDS.find(effectInstance.effectId)
                != -1
            ):
                damageBaseSpellModifier = (
                    spellmm.SpellModifiersManager().getSpellModifier(
                        entityId,
                        self.id,
                        CharacterSpellModificationTypeEnum.BASE_DAMAGE,
                    )
                )
                if damageBaseSpellModifier and effectInstance is EffectInstanceDice:
                    effectInstanceDice = effectInstance
                    modif = (
                        damageBaseSpellModifier.totalValue
                        - damageBaseSpellModifier.additionalValue
                    )
                    effectInstanceDice.diceNum += modif
                    if effectInstanceDice.diceSide > 0:
                        effectInstanceDice.diceSide += modif
                damageSpellModifier = spellmm.SpellModifiersManager().getSpellModifier(
                    entityId, self.id, CharacterSpellModificationTypeEnum.DAMAGE
                )
                healSpellModifier = spellmm.SpellModifiersManager().getSpellModifier(
                    entityId, self.id, CharacterSpellModificationTypeEnum.HEAL_BONUS
                )
                if damageSpellModifier:
                    effectInstance.modificator = (
                        damageSpellModifier.totalValue
                        - damageSpellModifier.additionalValue
                    )
                elif healSpellModifier:
                    effectInstance.modificator = (
                        damageSpellModifier.totalValue
                        - damageSpellModifier.additionalValue
                    )
            self.criticalEffect.append(effectInstance)
        llen = len(self._spellLevel.additionalEffectsZones)
        if llen > 0:
            self.additionalEffectsZones = list[EffectZone](0)
        for j in range(0, llen, 2):
            self.additionalEffectsZones.append(
                EffectZone(
                    self._spellLevel.additionalEffectsZones[j],
                    self._spellLevel.additionalEffectsZones[j + 1],
                )
            )
