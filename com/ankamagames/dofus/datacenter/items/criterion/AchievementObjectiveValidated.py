from com.ankamagames.dofus.datacenter.items.criterion.IItemCriterion import (
    IItemCriterion,
)
from com.ankamagames.dofus.datacenter.items.criterion.ItemCriterion import ItemCriterion
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter


class AchievementObjectiveValidated(ItemCriterion, IDataCenter):
    def __init__(self, pCriterion: str):
        super().__init__(pCriterion)

    # @property
    # def text(self) -> str:
    #    achievementObjective:AchievementObjective = AchievementObjective.getAchievementObjectiveById(_criterionValue)
    #    return I18n.getUiText("ui.achievement.objectiveValidated",[achievementObjective.name,Achievement.getAchievementById(achievementObjective.achievementId).name])

    def clone(self) -> IItemCriterion:
        return AchievementObjectiveValidated(self.basicText)
