from com.ankamagames.dofus.network.types.game.context.roleplay.job.JobDescription import (
    JobDescription,
)
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter


class KnownJobWrapper(IDataCenter):

    id: int

    jobDescription: JobDescription

    name: str

    iconId: int

    jobLevel: int = 0

    jobXP: float = 0

    jobXpLevelFloor: float = 0

    jobXpNextLevelFloor: float = 0

    jobBookSubscriber: bool = False

    def __init__(self):
        super().__init__()

    def create(self, id: int) -> "KnownJobWrapper":
        obj: KnownJobWrapper = KnownJobWrapper()
        obj.id = id
        job: Job = Job.getJobById(id)
        if job:
            obj.name = job.name
            obj.iconId = job.iconId
        return obj
