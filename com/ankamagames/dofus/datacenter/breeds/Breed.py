from com.ankamagames.dofus.datacenter.breeds.BreedRoleByBreed import BreedRoleByBreed
from com.ankamagames.dofus.datacenter.spells.Spell import Spell
from com.ankamagames.dofus.datacenter.spells.SpellVariant import SpellVariant
from com.ankamagames.jerakine.logger.Logger import Logger
from re import S
from com.ankamagames.dofus.types.IdAccessors import IdAccessors
from com.ankamagames.jerakine.data import I18n
from com.ankamagames.jerakine.data.GameData import GameData
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter

logger = Logger(__name__)


class Breed(IDataCenter):

    MODULE: str = "Breeds"

    _skinsForBreed: list = list()

    id: int

    shortNameId: int

    longNameId: int

    descriptionId: int

    gameplayDescriptionId: int

    gameplayClassDescriptionId: int

    maleLook: str

    femaleLook: str

    creatureBonesId: int

    maleArtwork: int

    femaleArtwork: int

    statsPointsForStrength: list[list[int]]

    statsPointsForIntelligence: list[list[int]]

    statsPointsForChance: list[list[int]]

    statsPointsForAgility: list[list[int]]

    statsPointsForVitality: list[list[int]]

    statsPointsForWisdom: list[list[int]]

    breedSpellsId: list[int]

    breedRoles: list[BreedRoleByBreed]

    maleColors: list[int]

    femaleColors: list[int]

    spawnMap: int

    complexity: int

    sortIndex: int

    _shortName: str

    _longName: str

    _description: str

    _gameplayDescription: str

    _gameplayClassDescription: str

    _allSpellsId: list

    _breedSpellsVariants: list[Spell]

    _breedSpellVariants: list[SpellVariant]

    def __init__(self):
        super().__init__()

    @staticmethod
    def getBreedById(id: int) -> "Breed":
        return GameData.getObject(Breed.MODULE, id)

    @staticmethod
    def getBreeds() -> list:
        return GameData.getobjects(Breed.MODULE)

    def getBreedFromSkin(self, skin: int) -> "Breed":
        skinKnown = None
        breed: Breed = None
        look: str = None
        id: int = 0
        if not len(self._skinsForBreed):
            for breed in self.getBreeds():
                look = breed.maleLook.split("|")[1]
                look = look.split(",")[0]
                self._skinsForBreed[look] = breed.id
                self._skinsForBreed[
                    SkinMapping.getSkinMappingById(int(look)).lowDefId
                ] = breed.id
                look = breed.femaleLook.split("|")[1]
                look = look.split(",")[0]
                self._skinsForBreed[look] = breed.id
                self._skinsForBreed[
                    SkinMapping.getSkinMappingById(int(look)).lowDefId
                ] = breed.id
        for skinKnown in self._skinsForBreed:
            if skinKnown == str(skin):
                id = self._skinsForBreed[skinKnown]
        return GameData.getObject(self.MODULE, id)

    @property
    def name(self) -> str:
        return self.shortName

    @property
    def shortName(self) -> str:
        if not self._shortName:
            self._shortName = I18n.getText(self.shortNameId)
        return self._shortName

    @property
    def longName(self) -> str:
        if not self._longName:
            self._longName = I18n.getText(self.longNameId)
        return self._longName

    @property
    def description(self) -> str:
        if not self._description:
            self._description = I18n.getText(self.descriptionId)
        return self._description

    @property
    def gameplayDescription(self) -> str:
        if not self._gameplayDescription:
            self._gameplayDescription = I18n.getText(self.gameplayDescriptionId)
        return self._gameplayDescription

    @property
    def gameplayClassDescription(self) -> str:
        if not self._gameplayClassDescription:
            self._gameplayClassDescription = I18n.getText(
                self.gameplayClassDescriptionId
            )
        return self._gameplayClassDescription

    @property
    def allSpellsId(self) -> list:
        variant: SpellVariant = None
        spellId: int = 0
        if not self._allSpellsId:
            self._allSpellsId = list()
            for variant in self.breedSpellVariants:
                for spellId in variant.spellIds:
                    self._allSpellsId.append(spellId)
        return self._allSpellsId

    @property
    def breedSpellVariants(self) -> list[SpellVariant]:
        spellVariants: list = None
        variant: SpellVariant = None
        if not self._breedSpellVariants:
            self._breedSpellVariants = list[SpellVariant]()
            spellVariants = SpellVariant.getSpellVariants()
            for variant in spellVariants:
                if variant.breedId == self.id:
                    self._breedSpellVariants.append(variant)
        return self._breedSpellVariants

    def getStatsPointsNeededForStrength(self, stat: int) -> int:
        i = None
        for i in self.statsPointsForStrength:
            if stat < self.statsPointsForStrength[i][0]:
                return self.statsPointsForStrength[i - 1][1]
        return self.statsPointsForStrength[i][1]

    def getStatsPointsNeededForIntelligence(self, stat: int) -> int:
        i = None
        for i in self.statsPointsForIntelligence:
            if stat < self.statsPointsForIntelligence[i][0]:
                return self.statsPointsForIntelligence[i - 1][1]
        return self.statsPointsForIntelligence[i][1]

    def getStatsPointsNeededForChance(self, stat: int) -> int:
        i = None
        for i in self.statsPointsForChance:
            if stat < self.statsPointsForChance[i][0]:
                return self.statsPointsForChance[i - 1][1]
        return self.statsPointsForChance[i][1]

    def getStatsPointsNeededForAgility(self, stat: int) -> int:
        i = None
        for i in self.statsPointsForAgility:
            if stat < self.statsPointsForAgility[i][0]:
                return self.statsPointsForAgility[i - 1][1]
        return self.statsPointsForAgility[i][1]

    def getStatsPointsNeededForVitality(self, stat: int) -> int:
        i = None
        for i in self.statsPointsForVitality:
            if stat < self.statsPointsForVitality[i][0]:
                return self.statsPointsForVitality[i - 1][1]
        return self.statsPointsForVitality[i][1]

    def getStatsPointsNeededForWisdom(self, stat: int) -> int:
        i = None
        for i in self.statsPointsForWisdom:
            if stat < self.statsPointsForWisdom[i][0]:
                return self.statsPointsForWisdom[i - 1][1]
        return self.statsPointsForWisdom[i][1]

    idAccessors: IdAccessors = IdAccessors(getBreedById, getBreeds)
