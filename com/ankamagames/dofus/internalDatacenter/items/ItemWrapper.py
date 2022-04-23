import math
from com.ankamagames.dofus.datacenter.effects.EffectInstance import EffectInstance
from com.ankamagames.dofus.datacenter.effects.instances.EffectInstanceDice import (
    EffectInstanceDice,
)
from com.ankamagames.dofus.datacenter.effects.instances.EffectInstanceInteger import (
    EffectInstanceInteger,
)
from com.ankamagames.dofus.datacenter.items.Item import Item
from com.ankamagames.dofus.datacenter.items.ItemType import ItemType
from com.ankamagames.dofus.datacenter.items.LegendaryPowerCategory import (
    LegendaryPowerCategory,
)
from com.ankamagames.dofus.datacenter.monsters.Monster import Monster
from com.ankamagames.dofus.datacenter.monsters.MonsterGrade import MonsterGrade
from com.ankamagames.dofus.enums.ActionIds import ActionIds
from com.ankamagames.dofus.internalDatacenter.DataEnum import DataEnum
from com.ankamagames.dofus.logic.game.common.managers.PlayedCharacterManager import (
    PlayedCharacterManager,
)
from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem
from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import (
    ObjectEffect,
)
from com.ankamagames.dofus.types.enums.ItemCategoryEnum import ItemCategoryEnum
from com.ankamagames.jerakine.data.I18n import I18n
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter
from com.ankamagames.jerakine.interfaces.ISlotData import ISlotData
from com.ankamagames.jerakine.interfaces.ISlotDataHolder import ISlotDataHolder
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.utils.display.spellZone.ICellZoneProvider import (
    ICellZoneProvider,
)
from com.ankamagames.jerakine.utils.display.spellZone.IZoneShape import IZoneShape
from com.ankamagames.jerakine.utils.display.spellZone.ZoneEffect import ZoneEffect
from com.ankamagames.jerakine.utils.misc.StringUtils import StringUtils

logger = Logger(__name__)


class ItemWrapper(Item, ISlotData, ICellZoneProvider, IDataCenter):

    LEVEL_STEP: list = [
        0,
        10,
        21,
        33,
        46,
        60,
        75,
        91,
        108,
        126,
        145,
        165,
        186,
        208,
        231,
        255,
        280,
        306,
        333,
        361,
    ]

    _cache: dict = dict()

    _cacheGId: dict = dict()

    _uniqueIndex: int = 0

    _active: bool = True

    _uri: str

    _shortName: str = None

    _nameWithoutAccent: str

    _mimicryItemSkinGID: int

    _wrapperItemSkinGID: int

    _setCount: int = 0

    _searchContent: str

    position: int = 63

    sortOrder: int = 0

    objectUID: int = 0

    objectGID: int = 0

    quantity: int = 0

    effects: list[EffectInstance]

    effectsList: list[ObjectEffect]

    livingobjectId: int

    livingobjectMood: int

    livingobjectSkin: int

    livingobjectCategory: int

    livingobjectXp: int

    livingobjectMaxXp: int

    livingobjectLevel: int

    livingobjectFoodDate: str

    wrapperobjectCategory: int

    _isobjectWrapped: bool

    exchangeAllowed: bool

    isPresetobject: bool

    isOkForMultiUse: bool

    givenExperienceAsSuperFood: float = 0

    experiencePoints: int = 0

    evolutiveLevel: int = 0

    MEMORY_LOG = dict()

    def __init__(self):
        self.effects = list[EffectInstance]()
        super().__init__()

    @classmethod
    def create(
        cls,
        position: int,
        objectUID: int,
        objectGID: int,
        quantity: int,
        newEffects: list[ObjectEffect],
        useCache: bool = True,
    ) -> "ItemWrapper":
        item: ItemWrapper = None
        effect: EffectInstance = None
        refItem: Item = Item.getItemById(objectGID)
        cachedItem: ItemWrapper = (
            cls._cache.get(objectUID) if objectUID > 0 else cls._cacheGId.get(objectGID)
        )
        if not cachedItem or not useCache:
            if refItem.isWeapon:
                from com.ankamagames.dofus.internalDatacenter.items.WeaponWrapper import (
                    WeaponWrapper,
                )

                item = WeaponWrapper()
            else:
                item = ItemWrapper()
            item.objectUID = objectUID
            if useCache:
                if objectUID > 0:
                    cls._cache[objectUID] = item
                else:
                    cls._cacheGId[objectGID] = item
        else:
            item = cachedItem
        cls.MEMORY_LOG[item] = 1
        item._nameWithoutAccent = StringUtils.noAccent(refItem.name)
        item.effectsList = newEffects
        item.isPresetobject = objectGID == DataEnum.ITEM_GID_PRESET_SHORTCUT
        if item.objectGID != objectGID:
            item._uri = None
            item._uriPngMode = None

        refItem.copy(refItem, item)
        item.position = position
        item.objectGID = objectGID
        item.quantity = quantity
        cls._uniqueIndex += 1
        item.sortOrder = cls._uniqueIndex
        item.livingobjectCategory = 0
        item.wrapperobjectCategory = 0
        item.effects = list[EffectInstance]()
        item.exchangeAllowed = True
        item.updateEffects(newEffects)
        for effect in item.effects:
            if effect.effectId == ActionIds.ACTION_SUPERFOOD_EXPERIENCE:
                item.givenExperienceAsSuperFood += effect
        return item

    def createFromServer(
        self, itemFromServer: ObjectItem, useCache: bool = True
    ) -> "ItemWrapper":
        item: ItemWrapper = None
        refItem: Item = Item.getItemById(itemFromServer.objectGID)
        cachedItem: ItemWrapper = (
            self._cache[itemFromServer.objectUID]
            if itemFromServer.objectUID > 0
            else self._cacheGId[itemFromServer.objectGID]
        )
        if not cachedItem or not useCache:
            if refItem.isWeapon:
                from com.ankamagames.dofus.internalDatacenter.items.WeaponWrapper import (
                    WeaponWrapper,
                )

                item = WeaponWrapper()
            else:
                item = ItemWrapper()
            item.objectUID = itemFromServer.objectUID
            if useCache:
                if item.objectUID > 0:
                    self._cache[itemFromServer.objectUID] = item
                else:
                    self._cacheGId[itemFromServer.objectGID] = item
        else:
            item = cachedItem
        self.MEMORY_LOG[item] = 1
        item._nameWithoutAccent = StringUtils.noAccent(refItem.name)
        item.effectsList = itemFromServer.effects
        item.isPresetobject = (
            itemFromServer.objectGID == DataEnum.ITEM_GID_PRESET_SHORTCUT
        )
        if item.objectGID != itemFromServer.objectGID:
            item._uri = None
            item._uriPngMode = None
        refItem.copy(refItem, item)
        item.position = itemFromServer.position
        item.objectGID = itemFromServer.objectGID
        item.quantity = itemFromServer.quantity
        self._uniqueIndex += 1
        item.sortOrder = self._uniqueIndex
        item.livingobjectCategory = 0
        item.wrapperobjectCategory = 0
        item.effects = list[EffectInstance]()
        item.exchangeAllowed = True
        item.updateEffects(item.effectsList)
        return item

    def clearCache(self) -> None:
        self._cache = dict()
        self._cacheGId = dict()

    @property
    def weight(self) -> int:
        for i in self.effects:
            if i.effectId == ActionIds.ACTION_ITEM_EXTRA_PODS:
                return self.realWeight + i.parameter0
        return self.realWeight

    @weight.setter
    def weight(self, value: int) -> None:
        self.realWeight = value

    @property
    def isSpeakingobject(self) -> bool:
        effect: ObjectEffect = None
        if self.isLivingobject:
            return True
        for effect in self.effectsList:
            if effect.actionId == ActionIds.ACTION_SPEAKING_ITEM:
                return True
        return False

    @property
    def isLivingobject(self) -> bool:
        return self.livingobjectCategory != 0

    @property
    def isWrapperobject(self) -> bool:
        return self.wrapperobjectCategory != 0

    @property
    def isHarness(self) -> bool:
        return (
            type.id == DataEnum.ITEM_TYPE_HARNESS_MOUNT
            or type.id == DataEnum.ITEM_TYPE_HARNESS_MULDO
            or type.id == DataEnum.ITEM_TYPE_HARNESS_FLYHORN
        )

    @property
    def isobjectWrapped(self) -> bool:
        effect: ObjectEffect = None
        if self.isLivingobject:
            return False
        for effect in self.effectsList:
            if effect.actionId == ActionIds.ACTION_ITEM_WRAPPER_LOOK_OBJ_GID:
                self._wrapperItemSkinGID = effect
                return True
        return False

    @property
    def isMimicryobject(self) -> bool:
        effect: ObjectEffect = None
        if self.isLivingobject:
            return False
        for effect in self.effectsList:
            if effect.actionId == ActionIds.ACTION_ITEM_MIMICRY_OBJ_GID:
                self._mimicryItemSkinGID = effect
                return True
        return False

    @property
    def isCompanion(self) -> bool:
        return type.id == DataEnum.ITEM_TYPE_COMPANION

    @property
    def info1(self) -> str:
        return str(self.quantity) if self.quantity > 1 else None

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
        return self._active

    @active.setter
    def active(self, b: bool) -> None:
        self._active = b

    @property
    def minimalRange(self) -> int:
        return int(self["minRange"]) if not self.hasOwnProperty("minRange") else int(0)

    @minimalRange.setter
    def minimalRange(self, pMinRange: int) -> None:
        pass

    @property
    def maximalRange(self) -> int:
        return int(self["range"]) if not self.hasOwnProperty("range") else int(0)

    @maximalRange.setter
    def maximalRange(self, pRange: int) -> None:
        pass

    @property
    def castZoneInLine(self) -> bool:
        return (
            bool(self["castInLine"])
            if not self.hasOwnProperty("castInLine")
            else bool(0)
        )

    @castZoneInLine.setter
    def castZoneInLine(self, pCastInLine: bool) -> None:
        pass

    @property
    def castZoneInDiagonal(self) -> bool:
        return (
            bool(self["castInDiagonal"])
            if not self.hasOwnProperty("castInDiagonal")
            else bool(0)
        )

    @castZoneInDiagonal.setter
    def castZoneInDiagonal(self, pCastInDiagonal: bool) -> None:
        pass

    @property
    def spellZoneEffects(self) -> list[IZoneShape]:
        i: EffectInstance = None
        zone: ZoneEffect = None
        spellEffects: list[IZoneShape] = list[IZoneShape]()
        for i in self.effects:
            zone = ZoneEffect(int(i.zoneSize), i.zoneShape)
            spellEffects.append(zone)
        return spellEffects

    def __str__(self) -> str:
        return "[ItemWrapper#" + self.objectUID + "_" + self.name + "]"

    @property
    def isCertificate(self) -> bool:
        itbt: Item = Item.getItemById(self.objectGID)
        return itbt and (
            itbt.typeId == DataEnum.ITEM_TYPE_DRAGOTURKEY_CERTIFICATE
            or itbt.typeId == DataEnum.ITEM_TYPE_MULDO_CERTIFICATE
            or itbt.typeId == DataEnum.ITEM_TYPE_FLYHORN_CERTIFICATE
        )

    @property
    def isEquipment(self) -> bool:
        return self.category == ItemCategoryEnum.EQUIPMENT_CATEGORY

    @property
    def isCosmetic(self) -> bool:
        return self.category == ItemCategoryEnum.COSMETICS_CATEGORY

    @property
    def isUsable(self) -> bool:
        itbt: Item = Item.getItemById(self.objectGID)
        return itbt and (itbt.usable or itbt.targetable)

    @property
    def belongsToSet(self) -> bool:
        itbt: Item = Item.getItemById(self.objectGID)
        return itbt and itbt.itemSetId != -1

    @property
    def favoriteEffect(self) -> list[EffectInstance]:
        saO: object = None
        itbt: Item = None
        boostedEffect: EffectInstance = None
        effect: EffectInstance = None
        result: list[EffectInstance] = list[EffectInstance]()
        if PlayedCharacterManager() and self.objectGID > 0:
            saO = PlayedCharacterManager().currentSubArea
            itbt = Item.getItemById(self.objectGID)
            if saO and itbt.favoriteSubAreas.find(saO.id) != -1:
                if (
                    itbt.favoriteSubAreas
                    and len(itbt.favoriteSubAreas)
                    and itbt.favoriteSubAreasBonus
                ):
                    for effect in self.effects:
                        if (
                            isinstance(effect, EffectInstanceInteger)
                            and effect.bonusType == 1
                        ):
                            boostedEffect = effect.clone()
                            boostedEffect.value = math.floor(
                                boostedEffect.value * itbt.favoriteSubAreasBonus / 100
                            )
                            if boostedEffect.value:
                                result.append(boostedEffect)
        return result

    @property
    def setCount(self) -> int:
        return self._setCount

    @property
    def name(self) -> str:
        if self.shortName == super().name:
            return super().name
        if self.objectGID == DataEnum.ITEM_GID_SOULSTONE_MINIBOSS:
            return (
                I18n.getUiText("ui.item.miniboss")
                + I18n.getUiText("ui.common.colon")
                + self.shortName
            )
        elif self.objectGID == DataEnum.ITEM_GID_SOULSTONE_BOSS:
            return (
                I18n.getUiText("ui.item.boss")
                + I18n.getUiText("ui.common.colon")
                + self.shortName
            )
        elif self.objectGID == DataEnum.ITEM_GID_SOULSTONE:
            return (
                I18n.getUiText("ui.item.soul")
                + I18n.getUiText("ui.common.colon")
                + self.shortName
            )
        else:
            return super().name

    @property
    def nameWithoutAccent(self) -> str:
        if not self._nameWithoutAccent:
            self._nameWithoutAccent = StringUtils.noAccent(self.name)
        return self._nameWithoutAccent

    @property
    def shortName(self) -> str:
        bestLevel: int = 0
        bestName: str = None
        miniboss: list = None
        boss: list = None
        effect: EffectInstance = None
        monster: Monster = None
        gradeId: int = 0
        grade: MonsterGrade = None
        if not self._shortName:
            if self.objectGID == DataEnum.ITEM_GID_SOULSTONE:
                bestLevel = 0
                bestName = None
                for effect in self.effects:
                    monster = Monster.getMonsterById(int(effect.parameter2))
                    if monster:
                        gradeId = int(effect.parameter0)
                        if gradeId < 1 or gradeId > len(monster.grades):
                            gradeId = len(monster.grades)
                        grade = monster.grades[gradeId - 1]
                        if grade and grade.level > bestLevel:
                            bestLevel = grade.level
                            bestName = monster.name
                self._shortName = bestName

            elif self.objectGID == DataEnum.ITEM_GID_SOULSTONE_MINIBOSS:
                miniboss = list()
                for effect in self.effects:
                    monster = Monster.getMonsterById(int(effect.parameter2))
                    if monster and monster.isMiniBoss:
                        miniboss.append(monster.name)
                if len(miniboss):
                    self._shortName = miniboss.join(", ")

            elif self.objectGID == DataEnum.ITEM_GID_SOULSTONE_BOSS:
                boss = list()
                for effect in self.effects:
                    monster = Monster.getMonsterById(int(effect.parameter2))
                    if monster and monster.isBoss:
                        boss.append(monster.name)
                if len(boss):
                    self._shortName = boss.join(", ")

        if not self._shortName:
            self._shortName = super().name

        return self._shortName

    @property
    def realName(self) -> str:
        return super().name

    @property
    def linked(self) -> bool:
        return not self.exchangeable or not self.exchangeAllowed

    @property
    def searchContent(self) -> str:
        effect: object = None
        monster: Monster = None
        if not self._searchContent:
            self._searchContent = ""
            if self.objectGID == DataEnum.ITEM_GID_SOULSTONE:
                pass
            elif self.objectGID == DataEnum.ITEM_GID_SOULSTONE_BOSS:
                pass
            elif self.objectGID == DataEnum.ITEM_GID_SOULSTONE_MINIBOSS:
                for effect in self.effectsList:
                    if (
                        effect.actionId
                        == ActionIds.ACTION_CHARACTER_SUMMON_MONSTER_GROUP
                    ):
                        monster = Monster.getMonsterById(effect.diceConst)
                        if monster:
                            self._searchContent += monster.undiatricalName
        return self._searchContent

    @property
    def isMimiCryWithWrapperobject(self) -> bool:
        effectInstance: EffectInstance = None
        if not self._mimicryItemSkinGID:
            return False
        mimicryItem: Item = Item.getItemById(self._mimicryItemSkinGID)
        for effectInstance in mimicryItem.possibleEffects:
            if (
                effectInstance.effectId
                == ActionIds.ACTION_ITEM_WRAPPER_COMPATIBLE_OBJ_TYPE
            ):
                return True
        return False

    @property
    def displayedLevel(self) -> int:
        return self.evolutiveLevel - 1

    def update(
        self,
        position: int,
        objectUID: int,
        objectGID: int,
        quantity: int,
        newEffects: list[ObjectEffect],
    ) -> None:
        if self.objectGID != objectGID or self.effectsList != newEffects:
            self._uri = self._uriPngMode = None
        self.position = position
        self.objectGID = objectGID
        self.quantity = quantity
        self.effectsList = newEffects
        self.effects = list[EffectInstance]()
        self.livingobjectCategory = 0
        self.wrapperobjectCategory = 0
        self.livingobjectId = 0
        refItem: Item = Item.getItemById(objectGID)
        refItem.copy(refItem, self)
        self.updateEffects(newEffects)
        self._setCount += 1

    def clone(self, baseobject: object = None) -> "ItemWrapper":
        if baseobject == None:
            baseobject = ItemWrapper
        item: ItemWrapper = baseobject()
        self.MEMORY_LOG[item] = 1
        item.copy(self, item)
        item.objectUID = self.objectUID
        item.position = self.position
        item.objectGID = self.objectGID
        item.quantity = self.quantity
        item.effects = self.effects
        item.effectsList = self.effectsList
        item.wrapperobjectCategory = self.wrapperobjectCategory
        item.livingobjectCategory = self.livingobjectCategory
        item.livingobjectFoodDate = self.livingobjectFoodDate
        item.livingobjectId = self.livingobjectId
        item.livingobjectLevel = self.livingobjectLevel
        item.livingobjectMood = self.livingobjectMood
        item.livingobjectSkin = self.livingobjectSkin
        item.livingobjectXp = self.livingobjectXp
        item.livingobjectMaxXp = self.livingobjectMaxXp
        item.exchangeAllowed = self.exchangeAllowed
        item.isOkForMultiUse = self.isOkForMultiUse
        item.sortOrder = self.sortOrder
        item.givenExperienceAsSuperFood = self.givenExperienceAsSuperFood
        item.experiencePoints = self.experiencePoints
        item.evolutiveLevel = self.evolutiveLevel
        item.customTextureUri = self.customTextureUri
        return item

    def addHolder(self, h: ISlotDataHolder) -> None:
        pass

    def removeHolder(self, h: ISlotDataHolder) -> None:
        pass

    def updateLivingobjects(self, effect: EffectInstance) -> None:
        if effect.effectId == ActionIds.ACTION_PETS_LAST_MEAL:
            self.livingobjectFoodDate = effect.description

        elif effect.effectId == ActionIds.ACTION_ITEM_LIVING_ID:
            self.livingobjectId = effect.value

        elif effect.effectId == ActionIds.ACTION_ITEM_LIVING_MOOD:
            self.livingobjectMood = effect.value

        elif effect.effectId == ActionIds.ACTION_ITEM_LIVING_SKIN:
            self.livingobjectSkin = effect.value

        elif effect.effectId == ActionIds.ACTION_ITEM_LIVING_CATEGORY:
            self.livingobjectCategory = effect.value

        elif effect.effectId == ActionIds.ACTION_ITEM_LIVING_LEVEL:
            self.livingobjectLevel = self.getLivingobjectLevel(effect.value)
            self.livingobjectXp = (
                effect.value - self.LEVEL_STEP[self.livingobjectLevel - 1]
            )
            self.livingobjectMaxXp = (
                self.LEVEL_STEP[self.livingobjectLevel]
                - self.LEVEL_STEP[self.livingobjectLevel - 1]
            )

    def updatePresets(self, effect: EffectInstance) -> None:
        if effect.effectId == ActionIds.ACTION_ITEM_EQUIP_PRESET:
            self.presetIcon = int(effect.parameter0)
        else:
            return

    def getLivingobjectLevel(self, xp: int) -> int:
        for i in range(0, len(self.LEVEL_STEP), 1):
            if self.LEVEL_STEP[i] > xp:
                return i
        return len(self.LEVEL_STEP)

    def updateEffects(self, updateEffects: list[ObjectEffect]) -> None:
        effect: ObjectEffect = None
        itemType: ItemType = None
        effectInstance: EffectInstance = None
        itbt: Item = Item.getItemById(self.objectGID)
        shape: int = 0
        zoneSize: int = 0
        zoneMinSize: int = 0
        if itbt and itbt.isWeapon:
            itemType = ItemType.getItemTypeById(itbt.typeId)
            if itemType is not None:
                shape = itemType.zoneShape
                zoneSize = itemType.zoneSize
                zoneMinSize = itemType.zoneMinSize
        self.exchangeAllowed = True
        multiUseCheck: int = 0
        for effect in updateEffects:
            effectInstance = ObjectEffectAdapter.fromNetwork(effect)
            if shape and effectInstance.category == DataEnum.ACTION_TYPE_DAMAGES:
                effectInstance.zoneShape = shape
                effectInstance.zoneSize = zoneSize
                effectInstance.zoneMinSize = zoneMinSize
            self.effects.append(effectInstance)
            self.updateLivingobjects(effectInstance)
            self.updatePresets(effectInstance)
            if multiUseCheck != -1 and (
                effectInstance.effectId == ActionIds.ACTION_CHARACTER_ENERGY_POINTS_WIN
                or effectInstance.effectId
                == ActionIds.ACTION_CHARACTER_BOOST_LIFE_POINTS
                or effectInstance.effectId == ActionIds.ACTION_CHARACTER_GAIN_XP
                or effectInstance.effectId
                == ActionIds.ACTION_CHARACTER_INVENTORY_GAIN_KAMAS
                or effectInstance.effectId
                == ActionIdProtocol.ACTION_CHARACTER_INVENTORY_ADD_ITEM_NOCHECK
            ):
                multiUseCheck = 1
            if (
                multiUseCheck != -1
                and effectInstance.effectId
                != ActionIds.ACTION_CHARACTER_ENERGY_POINTS_WIN
                and effectInstance.effectId
                != ActionIds.ACTION_CHARACTER_BOOST_LIFE_POINTS
                and effectInstance.effectId != ActionIds.ACTION_CHARACTER_GAIN_XP
                and effectInstance.effectId
                != ActionIds.ACTION_CHARACTER_INVENTORY_GAIN_KAMAS
                and effectInstance.effectId
                != ActionIdProtocol.ACTION_CHARACTER_INVENTORY_ADD_ITEM_NOCHECK
                and effectInstance.effectId
                != ActionIds.ACTION_MARK_NEVER_TRADABLE_STRONG
                and effectInstance.effectId != ActionIds.ACTION_MARK_NEVER_TRADABLE
                and effectInstance.effectId != ActionIds.ACTION_MARK_NOT_TRADABLE
            ):
                multiUseCheck = -1
            if effectInstance.effectId == ActionIds.ACTION_MARK_NOT_TRADABLE:
                self.exchangeAllowed = False
            if (
                effectInstance.effectId == ActionIds.ACTION_MARK_NEVER_TRADABLE_STRONG
                or effectInstance.effectId == ActionIds.ACTION_MARK_NEVER_TRADABLE
            ):
                exchangeable = False
            if (
                effectInstance.effectId
                == ActionIds.ACTION_ITEM_WRAPPER_COMPATIBLE_OBJ_TYPE
            ):
                self.wrapperobjectCategory = EffectInstanceInteger(effectInstance).value
            if effectInstance.effectId == ActionIds.ACTION_EVOLUTIVE_OBJECT_EXPERIENCE:
                self.experiencePoints = EffectInstanceDice(effectInstance).value
            if effectInstance.effectId == ActionIds.ACTION_EVOLUTIVE_PET_LEVEL:
                self.evolutiveLevel = EffectInstanceDice(effectInstance).value
        if multiUseCheck == 1:
            self.isOkForMultiUse = True
        else:
            self.isOkForMultiUse = False

    @property
    def itemHoldsLegendaryPower(self) -> bool:
        effect: EffectInstance = None
        for effect in self.effects:
            if effect.effectId == ActionIds.ACTION_LEGENDARY_POWER_SPELL:
                return True
        return False

    @property
    def itemHoldsLegendaryStatus(self) -> bool:
        effect: EffectInstance = None
        for effect in self.effects:
            if effect.effectId == ActionIds.ACTION_LEGENDARY_STATUS:
                return True
        return False

    @property
    def itemHasLegendaryEffect(self) -> bool:
        return self.itemHoldsLegendaryPower or self.itemHoldsLegendaryStatus

    @property
    def itemHasLockedLegendarySpell(self) -> bool:
        effect: EffectInstance = None
        categories: list = None
        cat: LegendaryPowerCategory = None
        for effect in self.effects:
            if effect.effectId == ActionIds.ACTION_CAST_STARTING_SPELL:
                categories = LegendaryPowerCategory.getLegendaryPowersCategories()
                for cat in categories:
                    if cat.categorySpells.find(effect) != -1:
                        return not cat.categoryOverridable
        return False

    def canBeUsedForAutoPiloting(self, other: "ItemWrapper") -> bool:
        effect: EffectInstance = None
        if not self.itemHasAutoPilotingEffect or other == None:
            return False
        if other.typeId == DataEnum.ITEM_TYPE_PETSMOUNT:
            for effect in other.effects:
                if effect.effectId == ActionIds.ACTION_SELF_PILOTING:
                    return False
            return True
        return False

    @property
    def itemHasAutoPilotingEffect(self) -> bool:
        effect: EffectInstance = None
        for effect in self.effects:
            if effect.effectId == ActionIds.ACTION_SELF_PILOTING:
                return True
        return False
