from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from com.ankamagames.dofus.datacenter.items.criterion.IItemCriterion import (
        IItemCriterion,
    )
import com.ankamagames.dofus.datacenter.items.criterion.ItemCriterionFactory as icf
from com.ankamagames.dofus.datacenter.items.criterion.ItemCriterionOperator import (
    ItemCriterionOperator,
)
from com.ankamagames.dofus.kernel.Kernel import Kernel
from com.ankamagames.jerakine.data.I18n import I18n
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter


class ArenaMaxDuelRankCriterion(icf.ItemCriterionFactory, IDataCenter):
    def __init__(self, pCriterion: str):
        super().__init__(pCriterion)

    @property
    def text(self) -> str:
        readableCriterionValue: str = str(self._criterionValue)
        readableCriterionRef: str = I18n.getUiText("ui.common.pvpMaxDuelRank")
        readableOperator = ">"
        if self._operator.text == ItemCriterionOperator.DIFFERENT:
            readableOperator = I18n.getUiText("ui.common.differentFrom") + " >"
        return (
            readableCriterionRef + " " + readableOperator + " " + readableCriterionValue
        )

    def clone(self) -> "IItemCriterion":
        return ArenaMaxDuelRankCriterion(self.basicText)

    def getCriterion(self) -> int:
        frame: PartyManagementFrame = (
            Kernel().getWorker().getFrame(PartyManagementFrame)
        )
        maxRank: int = 0
        if frame.arenaRankDuelInfos and frame.arenaRankDuelInfos.maxRank > maxRank:
            maxRank = frame.arenaRankDuelInfos.maxRank
        return maxRank
