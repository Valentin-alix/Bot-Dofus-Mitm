from com.ankamagames.dofus.datacenter.items.criterion.GroupItemCriterion import (
    GroupItemCriterion,
)
from com.ankamagames.dofus.datacenter.items.criterion.IItemCriterion import (
    IItemCriterion,
)
from com.ankamagames.dofus.datacenter.items.criterion.ItemCriterion import ItemCriterion
from com.ankamagames.jerakine.logger.Logger import Logger

logger = Logger(__name__)


class GroupFeatureCriterion(GroupItemCriterion):
    def __init__(self, criteria: str):
        super().__init__(criteria)

    @property
    def isRespected(self) -> bool:
        criterion: IItemCriterion = None
        if not self._criteria or len(self._criteria) == 0:
            return True
        if (
            self._criteria is not None
            and len(self._criteria) == 1
            and self._criteria[0] is ItemCriterion
        ):
            return self._criteria[0].isRespected
        if len(self._operators) > 0 and self._operators[0] == "|":
            for criterion in self._criteria:
                if criterion.isRespected:
                    return True
            return False
        for criterion in self._criteria:
            if not criterion.isRespected:
                return False
        return True
