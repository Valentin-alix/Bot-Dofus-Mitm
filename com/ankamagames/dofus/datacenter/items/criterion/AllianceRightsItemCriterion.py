from com.ankamagames.dofus.datacenter.items.criterion.IItemCriterion import (
    IItemCriterion,
)
from com.ankamagames.dofus.datacenter.items.criterion.ItemCriterion import ItemCriterion
from com.ankamagames.dofus.datacenter.items.criterion.ItemCriterionOperator import (
    ItemCriterionOperator,
)
from com.ankamagames.jerakine.data.I18n import I18n
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter


class AllianceRightsItemCriterion(ItemCriterion, IDataCenter):
    def __init__(self, pCriterion: str):
        super().__init__(pCriterion)

    @property
    def isRespected(self) -> bool:
        hasThisRight: bool = False
        if not AllianceFrame().hasAlliance:
            if self.operator.text == ItemCriterionOperator.DIFFERENT:
                return True
            return False
        alliance: AllianceWrapper = AllianceFrame().alliance
        if self.value == AllianceRightsBitEnum.ALLIANCE_RIGHT_BOSS:
            hasThisRight = alliance.isBoss
        else:
            hasThisRight = True
        if self.operator.text == ItemCriterionOperator.EQUAL:
            return hasThisRight
        if self.operator.text == ItemCriterionOperator.DIFFERENT:
            return not hasThisRight
        else:
            return False

    @property
    def text(self) -> str:
        readableCriterion: str = None
        readableCriterionValue: str = None
        if self.value == AllianceRightsBitEnum.ALLIANCE_RIGHT_BOSS:
            readableCriterionValue = I18n.getUiText("ui.guild.right.leader")
        if self.value == AllianceRightsBitEnum.ALLIANCE_RIGHT_KICK_GUILDS:
            readableCriterionValue = I18n.getUiText("ui.social.guildRightsBann")
        if self.value == AllianceRightsBitEnum.ALLIANCE_RIGHT_MANAGE_PRISMS:
            readableCriterionValue = I18n.getUiText(
                "ui.social.guildRightsSetAlliancePrism"
            )
        if self.value == AllianceRightsBitEnum.ALLIANCE_RIGHT_MANAGE_RIGHTS:
            readableCriterionValue = I18n.getUiText("ui.social.guildManageRights")
        if self.value == AllianceRightsBitEnum.ALLIANCE_RIGHT_RECRUIT_GUILDS:
            readableCriterionValue = I18n.getUiText("ui.social.guildRightsInvit")
        if self.value == AllianceRightsBitEnum.ALLIANCE_RIGHT_TALK_IN_CHAN:
            readableCriterionValue = I18n.getUiText(
                "ui.social.guildRightsTalkInAllianceChannel"
            )
        if self.operator.text == ItemCriterionOperator.EQUAL:
            readableCriterion = I18n.getUiText(
                "ui.criterion.allianceRights", [readableCriterionValue]
            )
        if self.operator.text == ItemCriterionOperator.DIFFERENT:
            readableCriterion = I18n.getUiText(
                "ui.criterion.notAllianceRights", [readableCriterionValue]
            )
        return readableCriterion

    def clone(self) -> IItemCriterion:
        return AllianceRightsItemCriterion(self.basicText)
