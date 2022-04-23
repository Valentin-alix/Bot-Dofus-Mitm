from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter


class BasicCharacterWrapper(IDataCenter):

    id: float

    name: str

    level: int

    breedId: int

    sex: bool

    deathState: int

    deathCount: int

    deathMaxLevel: int

    bonusXp: int

    unusable: bool

    # _breed:Breed

    def __init__(self):
        super().__init__()

    def create(
        self,
        id: float,
        name: str,
        level: int,
        entityLook: EntityLook,
        breed: int,
        sex: bool,
        deathState: int = 0,
        deathCount: int = 0,
        deathMaxLevel: int = 0,
        bonusXp: int = 0,
        unusable: bool = False,
    ) -> "BasicCharacterWrapper":
        obj: BasicCharacterWrapper = BasicCharacterWrapper()
        obj.id = id
        obj.name = name
        obj.level = level
        obj.breedId = breed
        # obj._breed = Breed.getBreedById(obj.breedId)
        obj.sex = sex
        obj.deathState = deathState
        obj.deathCount = deathCount
        obj.deathMaxLevel = deathMaxLevel
        obj.bonusXp = bonusXp
        obj.unusable = unusable
        return obj

    # @property
    # def breed(self) -> Breed:
    #    if not self._breed:
    #       self._breed = Breed.getBreedById(self.breedId)
    #    return self._breed

    def __str__(self) -> str:
        return "[BasicCharacterWrapper#" + self.id + "_" + self.name + "]"
