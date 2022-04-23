from com.ankamagames.dofus.datacenter.items.criterion.IItemCriterion import (
    IItemCriterion,
)
from com.ankamagames.dofus.datacenter.items.criterion.ItemCriterion import ItemCriterion
from com.ankamagames.dofus.logic.game.common.managers.PlayedCharacterManager import (
    PlayedCharacterManager,
)
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter


class AchievementPointsItemCriterion(ItemCriterion, IDataCenter):
    def __init__(self, pCriterion: str):
        super().__init__(pCriterion)

    def clone(self) -> IItemCriterion:
        return AchievementPointsItemCriterion(self.basicText)

    def getCriterion(self) -> int:
        return int(PlayedCharacterManager().achievementPoints)
