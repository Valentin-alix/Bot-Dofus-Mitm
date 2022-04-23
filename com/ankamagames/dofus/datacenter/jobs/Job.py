from com.ankamagames.dofus.types.IdAccessors import IdAccessors
from com.ankamagames.jerakine.data.GameData import GameData
from com.ankamagames.jerakine.data.I18n import I18n
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter


class Job(IDataCenter):

    MODULE: str = "Jobs"

    id: int

    nameId: int

    iconId: int

    hasLegendaryCraft: bool

    _name: str

    def __init__(self):
        super().__init__()

    @staticmethod
    def getJobById(id: int) -> "Job":
        return GameData.getObject(Job.MODULE, id)

    @staticmethod
    def getJobs() -> list["Job"]:
        return GameData.getobjects(Job.MODULE)

    idAccessors: IdAccessors = IdAccessors(getJobById, getJobs)

    @property
    def name(self) -> str:
        if not self._name:
            self._name = I18n.getText(self.nameId)
        return self._name
