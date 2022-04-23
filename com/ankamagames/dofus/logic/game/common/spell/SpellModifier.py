from com.ankamagames.dofus.enums.ActionIds import ActionIds
from com.ankamagames.dofus.network.enums.CharacterSpellModificationTypeEnum import (
    CharacterSpellModificationTypeEnum,
)


class SpellModifier:

    UNKNOWN_MODIFIER_NAME: str = "unknown"

    _entityId: float = None

    _spellId: float = None

    _id: float = 0

    _baseValue: float = 0

    _additionalValue: float = 0

    _objectsAndMountBonusValue: float = 0

    _alignGiftBonusValue: float = 0

    _contextModifValue: float = 0

    _totalValue: float = 0

    _name: str = None

    def __init__(
        self,
        id: float,
        baseValue: float,
        additionalValue: float,
        objectsAndMountBonusValue: float,
        alignGiftBonusValue: float,
        contextModifValue: float,
    ):
        super().__init__()
        self._id = id
        self._baseValue = baseValue
        self._additionalValue = additionalValue
        self._objectsAndMountBonusValue = objectsAndMountBonusValue
        self._alignGiftBonusValue = alignGiftBonusValue
        self._contextModifValue = contextModifValue
        self._totalValue = (
            self._baseValue
            + self._additionalValue
            + self._objectsAndMountBonusValue
            + self._alignGiftBonusValue
            + self._contextModifValue
        )
        self._name = self.getModifierName()

    def getSpellModifierIdFromActionId(self, actionId: float) -> float:
        if actionId == ActionIds.ACTION_BOOST_SPELL_RANGEABLE:
            return CharacterSpellModificationTypeEnum.RANGEABLE
        elif actionId == ActionIds.ACTION_BOOST_SPELL_DMG:
            return CharacterSpellModificationTypeEnum.DAMAGE
        elif actionId == ActionIds.ACTION_BOOST_SPELL_BASE_DMG:
            return CharacterSpellModificationTypeEnum.BASE_DAMAGE
        elif actionId == ActionIds.ACTION_BOOST_SPELL_HEAL:
            return CharacterSpellModificationTypeEnum.HEAL_BONUS
        elif actionId == ActionIds.ACTION_BOOST_SPELL_AP_COST:
            return CharacterSpellModificationTypeEnum.AP_COST
        elif actionId == ActionIds.ACTION_DEBOOST_SPELL_AP_COST:
            return CharacterSpellModificationTypeEnum.AP_COST
        elif actionId == ActionIds.ACTION_BOOST_SPELL_CAST_INTVL:
            return CharacterSpellModificationTypeEnum.CAST_INTERVAL
        elif actionId == ActionIds.ACTION_BOOST_SPELL_CAST_INTVL_SET:
            return CharacterSpellModificationTypeEnum.CAST_INTERVAL_SET
        elif actionId == ActionIds.ACTION_BOOST_SPELL_CC:
            return CharacterSpellModificationTypeEnum.CRITICAL_HIT_BONUS
        elif actionId == ActionIds.ACTION_BOOST_SPELL_CASTOUTLINE:
            return CharacterSpellModificationTypeEnum.CAST_LINE
        elif actionId == ActionIds.ACTION_BOOST_SPELL_NOLINEOFSIGHT:
            return CharacterSpellModificationTypeEnum.LOS
        elif actionId == ActionIds.ACTION_BOOST_SPELL_MAXPERTURN:
            return CharacterSpellModificationTypeEnum.MAX_CAST_PER_TURN
        elif actionId == ActionIds.ACTION_BOOST_SPELL_MAXPERTARGET:
            return CharacterSpellModificationTypeEnum.MAX_CAST_PER_TARGET
        elif actionId == ActionIds.ACTION_BOOST_SPELL_RANGE_MAX:
            return CharacterSpellModificationTypeEnum.RANGE_MAX
        elif actionId == ActionIds.ACTION_DEBOOST_SPELL_RANGE_MAX:
            return CharacterSpellModificationTypeEnum.RANGE_MAX
        elif actionId == ActionIds.ACTION_BOOST_SPELL_RANGE_MIN:
            return CharacterSpellModificationTypeEnum.RANGE_MIN
        elif actionId == ActionIds.ACTION_DEBOOST_SPELL_RANGE_MIN:
            return CharacterSpellModificationTypeEnum.RANGE_MIN
        else:
            return CharacterSpellModificationTypeEnum.INVALID_MODIFICATION

    @property
    def entityId(self) -> float:
        return self._entityId

    @entityId.setter
    def entityId(self, entityId: float) -> None:
        self._entityId = entityId

    @property
    def spellId(self) -> float:
        return self._spellId

    @spellId.setter
    def spellId(self, spellId: float) -> None:
        self._spellId = spellId

    @property
    def id(self) -> float:
        return self._id

    @property
    def baseValue(self) -> float:
        return self._baseValue

    @property
    def additionalValue(self) -> float:
        return self._additionalValue

    @property
    def objectsAndMountBonusValue(self) -> float:
        return self._objectsAndMountBonusValue

    @property
    def alignGiftBonusValue(self) -> float:
        return self._alignGiftBonusValue

    @property
    def contextModifValue(self) -> float:
        return self._contextModifValue

    @property
    def totalValue(self) -> float:
        return self._totalValue

    def getModifierName(self) -> str:
        if self._id == CharacterSpellModificationTypeEnum.INVALID_MODIFICATION:
            return "invalid modification"
        if self._id == CharacterSpellModificationTypeEnum.RANGEABLE:
            return "rangeable"
        if self._id == CharacterSpellModificationTypeEnum.DAMAGE:
            return "damage"
        if self._id == CharacterSpellModificationTypeEnum.BASE_DAMAGE:
            return "base damage"
        if self._id == CharacterSpellModificationTypeEnum.HEAL_BONUS:
            return "heal bonus"
        if self._id == CharacterSpellModificationTypeEnum.AP_COST:
            return "ap cost"
        if self._id == CharacterSpellModificationTypeEnum.CAST_INTERVAL:
            return "cast interval"
        if self._id == CharacterSpellModificationTypeEnum.CAST_INTERVAL_SET:
            return "cast interval set"
        if self._id == CharacterSpellModificationTypeEnum.CRITICAL_HIT_BONUS:
            return "critical hit bonus"
        if self._id == CharacterSpellModificationTypeEnum.CAST_LINE:
            return "cast line"
        if self._id == CharacterSpellModificationTypeEnum.LOS:
            return "los"
        if self._id == CharacterSpellModificationTypeEnum.MAX_CAST_PER_TURN:
            return "max cast per turn"
        if self._id == CharacterSpellModificationTypeEnum.MAX_CAST_PER_TARGET:
            return "max cast per target"
        if self._id == CharacterSpellModificationTypeEnum.RANGE_MAX:
            return "range max"
        if self._id == CharacterSpellModificationTypeEnum.RANGE_MIN:
            return "range min"
        else:
            return self.UNKNOWN_MODIFIER_NAME

    def __str__(self) -> str:
        return (
            self.__class__.__name__
            + " "
            + self._name
            + " (Entity ID: "
            + str(self._entityId)
            + ", Spell ID: "
            + str(self._spellId)
            + ", ID: "
            + str(self._id)
            + "): "
            + "base: "
            + str(self._baseValue)
            + " additional: "
            + str(self._additionalValue)
            + " objectsAndMountBonus: "
            + str(self._objectsAndMountBonusValue)
            + " alignGiftBonus: "
            + str(self._alignGiftBonusValue)
            + " contextModif: "
            + str(self._contextModifValue)
            + " total: "
            + str(self._totalValue)
        )
