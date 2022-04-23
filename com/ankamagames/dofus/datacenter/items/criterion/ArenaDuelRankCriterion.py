from com.ankamagames.dofus.datacenter.items.criterion.IItemCriterion import (
    IItemCriterion,
)
from com.ankamagames.dofus.datacenter.items.criterion.ItemCriterion import ItemCriterion
from com.ankamagames.dofus.datacenter.items.criterion.ItemCriterionOperator import (
    ItemCriterionOperator,
)
from com.ankamagames.jerakine.data.I18n import I18n
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter


class ArenaDuelRankCriterion(ItemCriterion, IDataCenter):
    def __init__(self, pCriterion: str):
        super().__init__(pCriterion)

    @property
    def text(self) -> str:
        readableCriterionValue: str = str(self._criterionValue)
        readableCriterionRef: str = I18n.getUiText("ui.common.pvpDuelRank")
        readableOperator = ">"
        if self._operator.text == ItemCriterionOperator.DIFFERENT:
            readableOperator = I18n.getUiText("ui.common.differentFrom") + " >"
        return (
            readableCriterionRef + " " + readableOperator + " " + readableCriterionValue
        )

    def clone(self) -> IItemCriterion:
        return ArenaDuelRankCriterion(self.basicText)

    def getCriterion(self) -> int:
        from com.ankamagames.dofus.kernel.Kernel import Kernel

        frame: PartyManagementFrame = (
            Kernel().getWorker().getFrame(PartyManagementFrame)
        )
        rank: int = 0
        if frame.arenaRankDuelInfos and frame.arenaRankDuelInfos.rank > rank:
            rank = frame.arenaRankDuelInfos.rank
        return rank
