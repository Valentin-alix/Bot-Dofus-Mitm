from com.ankamagames.dofus.datacenter.interactives.Interactive import Interactive
from com.ankamagames.dofus.datacenter.jobs.Job import Job
from com.ankamagames.dofus.internalDatacenter.items.ItemWrapper import ItemWrapper
from com.ankamagames.dofus.types.IdAccessors import IdAccessors
from com.ankamagames.jerakine.data.GameData import GameData
from com.ankamagames.jerakine.data.I18n import I18n
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter


class Skill(IDataCenter):

    MODULE: str = "Skills"

    id: int

    nameId: int

    parentJobId: int

    isForgemagus: bool

    modifiableItemTypeIds: list[int]

    gatheredRessourceItem: int

    craftableItemIds: list[int]

    interactiveId: int

    range: int

    useRangeInClient: bool

    useAnimation: str

    cursor: int

    elementActionId: int

    availableInHouse: bool

    levelMin: int

    clientDisplay: bool

    _name: str

    _parentJob: Job

    _interactive: Interactive

    _gatheredRessource: ItemWrapper

    def __init__(self):
        super().__init__()

    @classmethod
    def getSkillById(cls, id: int) -> "Skill":
        return GameData.getObject(cls.MODULE, id)

    @classmethod
    def getSkills(cls) -> list["Skill"]:
        return GameData.getObjects(cls.MODULE)

    idAccessors: IdAccessors = IdAccessors(getSkillById, getSkills)

    @property
    def name(self) -> str:
        if not self._name:
            self._name = I18n.getText(self.nameId)
        return self._name

    @property
    def parentJob(self) -> Job:
        if not self._parentJob:
            self._parentJob = Job.getJobById(self.parentJobId)
        return self._parentJob

    @property
    def interactive(self) -> Interactive:
        if not self._interactive:
            self._interactive = Interactive.getInteractiveById(self.interactiveId)
        return self._interactive

    @property
    def gatheredRessource(self) -> ItemWrapper:
        if not self._gatheredRessource and self.gatheredRessourceItem != -1:
            self._gatheredRessource = ItemWrapper.create(
                0, 0, self.gatheredRessourceItem, 1, None, False
            )
        return self._gatheredRessource
