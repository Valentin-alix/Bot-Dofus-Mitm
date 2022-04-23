import re
from typing import Any
from com.ankamagames.dofus.datacenter.spells.SpellType import SpellType
from com.ankamagames.dofus.datacenter.spells.SpellVariant import SpellVariant
from com.ankamagames.dofus.types.IdAccessors import IdAccessors
from com.ankamagames.jerakine.data.GameData import GameData
from com.ankamagames.jerakine.data.I18n import I18n
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter
from com.ankamagames.jerakine.logger.Logger import Logger

logger = Logger(__name__)


class Spell(IDataCenter):

    MODULE: str = "Spells"

    _indexedParam: list

    _indexedCriticalParam: list

    id: int

    nameId: int

    descriptionId: int

    typeId: int

    order: int

    scriptParams: str

    scriptParamsCritical: str

    scriptId: int

    scriptIdCritical: int

    iconId: int

    spellLevels: list[int]

    useParamCache: bool = True

    verbose_cast: bool

    default_zone: str

    bypassSummoningLimit: bool

    canAlwaysTriggerSpells: bool

    adminName: str

    _name: str

    _description: str

    _spellLevels: list

    _spellVariant: SpellVariant

    def __init__(self):
        self._spellLevels = []
        super().__init__()

    @classmethod
    def getSpellById(cls, id: int) -> "Spell":
        return GameData.getObject(cls.MODULE, id)

    @classmethod
    def getSpells(cls) -> list["Spell"]:
        return GameData.getObjects(cls.MODULE)

    idAccessors: IdAccessors = IdAccessors(getSpellById, getSpells)

    @property
    def name(self) -> str:
        if not self._name:
            self._name = I18n.getText(self.nameId)
        return self._name

    @property
    def description(self) -> str:
        if not self._description:
            self._description = I18n.getText(self.descriptionId)
        return self._description

    @property
    def type(self) -> SpellType:
        return SpellType.getSpellTypeById(self.typeId)

    @property
    def spellVariant(self) -> SpellVariant:
        allSpellVariants: list = None
        variant: SpellVariant = None
        if not self._spellVariant:
            allSpellVariants = SpellVariant.getSpellVariants()
            for variant in allSpellVariants:
                if variant.spellIds.find(self.id) != -1:
                    self._spellVariant = variant
                    return self._spellVariant
        return self._spellVariant

    def getSpellLevel(self, level: int):
        self.spellLevelsInfo
        index: int = 0
        if len(self.spellLevels) >= level and level > 0:
            index = level - 1
        return self._spellLevels[index]

    @property
    def spellLevelsInfo(self) -> list:
        from com.ankamagames.dofus.datacenter.spells.SpellLevel import SpellLevel

        if not self._spellLevels or len(self._spellLevels) != len(self.spellLevels):
            levelCount = len(self.spellLevels)
            for i in range(levelCount):
                self._spellLevels[i] = SpellLevel.getLevelById(self.spellLevels[i])
                i += 1
        return self._spellLevels

    def getScriptId(self, critical: bool = False) -> int:
        if critical and self.scriptIdCritical:
            return self.scriptIdCritical
        return self.scriptId

    def getParamByName(self, name: str, critical: bool = False) -> Any:
        tmp: list = None
        tmp2: list = None
        param: str = None
        if (
            critical
            and self.scriptParamsCritical
            and self.scriptParamsCritical != "None"
        ):
            if not self._indexedCriticalParam or not self.useParamCache:
                self._indexedCriticalParam = list()
                if self.scriptParamsCritical:
                    tmp = self.scriptParamsCritical.split(",")
                    for param in tmp:
                        tmp2 = param.split(":")
                        self._indexedCriticalParam[tmp2[0]] = self.getValue(tmp2[1])
            return self._indexedCriticalParam[name]
        if not self._indexedParam or not self.useParamCache:
            self._indexedParam = list()
            if self.scriptParams:
                tmp = self.scriptParams.split(",")
                for param in tmp:
                    tmp2 = param.split(":")
                    self._indexedParam[tmp2[0]] = self.getValue(tmp2[1])
        return self._indexedParam[name]

    def getValue(self, str: str) -> Any:
        regNum = "^[+-]?[0-9.]*$"
        m = re.fullmatch(regNum, str)
        if m:
            num = float(str)
            return 0 if num is None else num
        return str

    def __str__(self) -> str:
        return self.name + " (" + str(self.id) + ")"
