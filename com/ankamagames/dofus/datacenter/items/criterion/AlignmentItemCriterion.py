from com.ankamagames.dofus.datacenter.alignments.AlignmentSide import AlignmentSide
from com.ankamagames.dofus.datacenter.items.criterion.IItemCriterion import (
    IItemCriterion,
)
from com.ankamagames.dofus.datacenter.items.criterion.ItemCriterion import ItemCriterion
from com.ankamagames.dofus.datacenter.items.criterion.ItemCriterionOperator import (
    ItemCriterionOperator,
)
from com.ankamagames.dofus.logic.game.common.managers.PlayedCharacterManager import (
    PlayedCharacterManager,
)
from com.ankamagames.jerakine.data.I18n import I18n
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter


class AlignmentItemCriterion(ItemCriterion, IDataCenter):
    def __init__(self, pCriterion: str):
        super().__init__(pCriterion)

    @property
    def text(self) -> str:
        readableCriterionValue: str = AlignmentSide.getAlignmentSideById(
            int(self._criterionValue)
        ).name
        readableCriterionRef: str = I18n.getUiText("ui.common.alignment")
        readableOperator: str = ":"
        if self._operator.text == ItemCriterionOperator.DIFFERENT:
            readableOperator = I18n.getUiText(
                "ui.common.differentFrom"
            ) + I18n.getUiText("ui.common.colon")
        return (
            readableCriterionRef + " " + readableOperator + " " + readableCriterionValue
        )

    def clone(self) -> IItemCriterion:
        return AlignmentItemCriterion(self.basicText)

    def getCriterion(self) -> int:
        return PlayedCharacterManager().characteristics.alignmentInfos.alignmentSide
