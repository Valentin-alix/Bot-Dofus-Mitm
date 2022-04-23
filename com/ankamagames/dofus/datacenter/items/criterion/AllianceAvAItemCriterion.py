from com.ankamagames.dofus.datacenter.items.criterion.IItemCriterion import (
    IItemCriterion,
)
from com.ankamagames.dofus.datacenter.items.criterion.ItemCriterionOperator import (
    ItemCriterionOperator,
)
from com.ankamagames.dofus.datacenter.world.SubArea import SubArea
from com.ankamagames.dofus.logic.game.common.managers.PlayedCharacterManager import (
    PlayedCharacterManager,
)
from com.ankamagames.dofus.network.enums.AggressableStatusEnum import (
    AggressableStatusEnum,
)
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter


class AllianceAvAItemCriterion(IItemCriterion, IDataCenter):
    def __init__(self, pCriterion: str):
        super().__init__(pCriterion)

    @property
    def isRespected(self) -> bool:
        aggressable: int = 0
        subArea: SubArea = None
        currentPrism: PrismSubAreaWrapper = None
        if self._operator.text == ItemCriterionOperator.EQUAL:
            aggressable = (
                PlayedCharacterManager().characteristics.alignmentInfos.aggressable
            )
            if (
                aggressable != AggressableStatusEnum.AvA_ENABLED_AGGRESSABLE
                and aggressable != AggressableStatusEnum.AvA_PREQUALIFIED_AGGRESSABLE
            ):
                return False
            subArea = PlayedCharacterManager().currentSubArea
            currentPrism = AllianceFrame().getPrismSubAreaById(subArea.id)
            if not currentPrism or currentPrism.mapId == -1:
                return False
            if currentPrism.state != PrismStateEnum.PRISM_STATE_VULNERABLE:
                return False
            return True
        return False

    @property
    def text(self) -> str:
        readableCriterion: str = None
        if self._operator.text == ItemCriterionOperator.EQUAL:
            readableCriterion = I18n.getUiText("ui.criterion.allianceAvA")
        return readableCriterion

    def clone(self) -> IItemCriterion:
        return AllianceAvAItemCriterion(self.basicText)
