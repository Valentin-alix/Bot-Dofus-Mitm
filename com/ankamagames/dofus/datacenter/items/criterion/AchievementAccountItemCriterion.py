from com.ankamagames.dofus.datacenter.items.criterion.IItemCriterion import (
    IItemCriterion,
)
from com.ankamagames.dofus.datacenter.items.criterion.ItemCriterion import ItemCriterion
from com.ankamagames.dofus.datacenter.items.criterion.ItemCriterionOperator import (
    ItemCriterionOperator,
)
from com.ankamagames.dofus.kernel.Kernel import Kernel
from com.ankamagames.dofus.logic.common.managers.PlayerManager import PlayerManager
from com.ankamagames.dofus.logic.game.common.managers.PlayedCharacterManager import (
    PlayedCharacterManager,
)
from com.ankamagames.dofus.network.enums.GameServerTypeEnum import GameServerTypeEnum
from com.ankamagames.dofus.network.types.game.achievement.Achievement import Achievement
from com.ankamagames.dofus.network.types.game.achievement.AchievementAchieved import (
    AchievementAchieved,
)
from com.ankamagames.jerakine.data import I18n
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter


class AchievementAccountItemCriterion(ItemCriterion, IDataCenter):
    def __init__(self, pCriterion: str):
        super().__init__(pCriterion)

    @property
    def isRespected(self) -> bool:
        serverType: int = PlayerManager().server.gameTypeId
        if self._operator.text == ItemCriterionOperator.DIFFERENT:
            if (
                self.getCriterion() == 0
                or serverType == GameServerTypeEnum.SERVER_TYPE_EPIC
            ):
                return True
            return False
        if self.getCriterion() == 1:
            return True
        return False

    @property
    def text(self) -> str:
        readableValue = (
            " '" + Achievement.getAchievementById(self._criterionValue).name + "'"
        )
        readableCriterion: str = I18n.getUiText(
            "ui.tooltip.unlockAchievement", [readableValue]
        )
        if self._operator.text == ItemCriterionOperator.DIFFERENT:
            readableCriterion = I18n.getUiText(
                "ui.tooltip.dontUnlockAchievement", [readableValue]
            )
        return readableCriterion

    def clone(self) -> IItemCriterion:
        return AchievementAccountItemCriterion(self.basicText)

    def getCriterion(self) -> int:
        ach: AchievementAchieved = None
        achievementFinishedList: list[AchievementAchieved] = (
            Kernel().getWorker().getFrame(QuestFrame)
        )
        characterId: float = PlayedCharacterManager().id
        for ach in achievementFinishedList:
            if ach.id == self._criterionValue and ach.achievedBy != characterId:
                return 1
        return 0
