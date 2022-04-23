from com.ankamagames.dofus.logic.game.common.spell.SpellModifier import SpellModifier
from com.ankamagames.dofus.logic.game.common.spell.SpellModifiers import SpellModifiers
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterSpellModification import (
    CharacterSpellModification,
)
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.jerakine.managers.StoreDataManager import StoreDataManager
from com.ankamagames.jerakine.metaclasses.Singleton import Singleton
from com.ankamagames.jerakine.types.DataStoreType import DataStoreType
from com.ankamagames.jerakine.types.enums.DataStoreEnum import DataStoreEnum

logger = Logger(__name__)


class SpellModifiersManager(metaclass=Singleton):

    _dataStoreType: DataStoreType = None

    DATA_STORE_CATEGORY: str = "ComputerModule_spellModifiersManager"

    DATA_STORE_KEY_IS_VERBOSE: str = "spellModifiersManagerIsVerbose"

    DEFAULT_IS_VERBOSE: bool = False

    _entitiesMap: dict

    _isVerbose: bool

    def __init__(self):
        self._entitiesMap = dict()
        self._isVerbose = self.DEFAULT_IS_VERBOSE
        super().__init__()
        logger.info("Instantiating spells manager")
        if _dataStoreType is None:
            _dataStoreType = DataStoreType(
                self.DATA_STORE_CATEGORY,
                True,
                DataStoreEnum.LOCATION_LOCAL,
                DataStoreEnum.BIND_COMPUTER,
            )
        rawIsVerbose = StoreDataManager().getData(
            _dataStoreType, self.DATA_STORE_KEY_IS_VERBOSE
        )
        self._isVerbose = (
            rawIsVerbose if isinstance(rawIsVerbose, bool) else self.DEFAULT_IS_VERBOSE
        )

    @property
    def isVerbose(self) -> bool:
        return self._isVerbose

    @isVerbose.setter
    def isVerbose(self, isVerbose: bool) -> None:
        if self._isVerbose == isVerbose:
            return
        self._isVerbose = isVerbose
        StoreDataManager().setData(
            self._dataStoreType, self.DATA_STORE_KEY_IS_VERBOSE, self._isVerbose
        )
        verboseAction: str = "enabled" if self._isVerbose else "disabled"
        logger.info("Verbose mode has been " + verboseAction)

    def reset(self) -> None:
        _singleton = None
        logger.info("Singleton instance has been destroyed")

    def setSpellModifiers(self, spellModifiers: SpellModifiers) -> bool:
        spellsModifierStats: dict = None
        if spellModifiers == None:
            logger.error("Tried to set None spell modifier stats. Aborting")
            return False
        entityKey: str = str(spellModifiers.entityId)
        spellKey: str = str(spellModifiers.spellId)
        if entityKey not in self._entitiesMap:
            spellsModifierStats = self._entitiesMap[entityKey] = dict()
        else:
            spellsModifierStats = self._entitiesMap[entityKey]
        spellsModifierStats[spellKey] = spellModifiers
        return True

    def getSpellModifiers(self, entityId: float, spellId: float) -> SpellModifiers:
        entityKey: str = str(entityId)
        if entityKey not in self._entitiesMap:
            return None
        spellsModifierStats: dict = self._entitiesMap.get(entityKey)
        spellKey: str = str(spellId)
        if spellsModifierStats == None or spellKey not in spellsModifierStats:
            return None
        return spellsModifierStats[spellKey]

    def getSpellModifier(
        self, entityId: float, spellId: float, modifierId: float
    ) -> SpellModifier:
        spellModifiers: SpellModifiers = self.getSpellModifiers(entityId, spellId)
        if spellModifiers is not None:
            return spellModifiers.getModifier(modifierId)
        return None

    def setRawSpellsModifiers(
        self, entityId: float, rawSpellsModifiers: list[CharacterSpellModification]
    ) -> None:
        spellModifiers: SpellModifiers = None
        spellModifier: SpellModifier = None
        rawSpellModifier: CharacterSpellModification = None
        entityKey: str = str(entityId)
        spellsModifierStats: dict = dict()
        self._entitiesMap[entityKey] = dict()
        if rawSpellsModifiers is not None and len(rawSpellsModifiers) > 0:
            spellModifier = None
            for rawSpellModifier in rawSpellsModifiers:
                spellModifiers = spellsModifierStats[str(rawSpellModifier.spellId)]
                if spellModifiers == None:
                    spellModifiers = SpellModifiers(entityId, rawSpellModifier.spellId)
                    self.setSpellModifiers(spellModifiers)
                spellModifier = SpellModifier(
                    rawSpellModifier.modificationType,
                    rawSpellModifier.value.base,
                    rawSpellModifier.value.additional,
                    rawSpellModifier.value.objectsAndMountBonus,
                    rawSpellModifier.value.alignGiftBonus,
                    rawSpellModifier.value.contextModif,
                )
                spellModifiers.setModifier(spellModifier)

    def setRawSpellModifier(
        self, entityId: float, rawSpellModifier: CharacterSpellModification
    ) -> None:
        if rawSpellModifier == None:
            return
        entityKey: str = str(entityId)
        spellsModifierStats: dict = self._entitiesMap[entityKey]
        if spellsModifierStats == None:
            spellsModifierStats = self._entitiesMap[entityKey] = dict()
        spellKey: str = str(rawSpellModifier.spellId)
        spellModifiers: SpellModifiers = spellsModifierStats[spellKey]
        if spellModifiers == None:
            spellModifiers = spellsModifierStats[spellKey] = SpellModifiers(
                entityId, rawSpellModifier.spellId
            )
        spellModifier: SpellModifier = SpellModifier(
            rawSpellModifier.modificationType,
            rawSpellModifier.value.base,
            rawSpellModifier.value.additional,
            rawSpellModifier.value.objectsAndMountBonus,
            rawSpellModifier.value.alignGiftBonus,
            rawSpellModifier.value.contextModif,
        )
        spellModifiers.setModifier(spellModifier)

    def deleteSpellsModifiers(self, entityId: float) -> bool:
        key: str = str(entityId)
        if key not in self._entitiesMap:
            logger.error(
                "Tried to del spells modifier stats for entity with ID "
                + key
                + ", but none were found. Aborting"
            )
            return False
        del self._entitiesMap[key]
        logger.info("Spells modifiers for entity with ID " + key + " deleted")
        return True

    def deleteSpellModifiers(self, entityId: float, spellId: float) -> bool:
        entityKey: str = str(entityId)
        spellKey: str = str(spellId)
        if entityKey not in self._entitiesMap:
            logger.error(
                "Tried to del spell "
                + spellKey
                + " modifiers for entity with ID "
                + entityKey
                + ", but no spells modifier stats were found. Aborting"
            )
            return False
        spellModifiers: SpellModifiers = self._entitiesMap[entityKey]
        if not spellModifiers or spellKey not in spellModifiers:
            logger.error(
                "Tried to del spell "
                + spellKey
                + " modifiers for entity with ID "
                + entityKey
                + ", but none were found. Aborting"
            )
            return False
        del spellModifiers[spellKey]
        logger.info(
            "Spell "
            + spellKey
            + " modifiers for entity with ID "
            + entityKey
            + " deleted"
        )
        return True

    def destroy(self) -> None:
        _singleton = None
