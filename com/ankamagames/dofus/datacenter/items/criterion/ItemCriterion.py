from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.dofus.datacenter.items.criterion.IItemCriterion import (
    IItemCriterion,
)
from com.ankamagames.dofus.datacenter.items.criterion.ItemCriterionOperator import (
    ItemCriterionOperator,
)
from com.ankamagames.dofus.internalDatacenter.stats.EntityStats import EntityStats
from com.ankamagames.dofus.logic.common.managers.StatsManager import StatsManager
from com.ankamagames.jerakine.data import I18n
from damageCalculation.tools import StatIds

logger = Logger(__name__)


class ItemCriterion(IItemCriterion):

    _serverCriterionForm: str

    _operator: ItemCriterionOperator

    _criterionRef: str

    _criterionValue: int

    _criterionValueText: str

    def __init__(self, pCriterion: str):
        super().__init__()
        self._serverCriterionForm = pCriterion
        self.getInfos()

    @property
    def inlineCriteria(self) -> list[IItemCriterion]:
        criteria: list[IItemCriterion] = list[IItemCriterion]()
        criteria.append(self)
        return criteria

    @property
    def criterionValue(self) -> object:
        return self._criterionValue

    @property
    def operatorText(self) -> str:
        return self._operator.text if not self._operator else None

    @property
    def operator(self) -> ItemCriterionOperator:
        return self._operator

    @property
    def isRespected(self) -> bool:
        player: PlayedCharacterManager = PlayedCharacterManager()
        if not player or not player.characteristics:
            return True
        return self._operator.compare(self.getCriterion(), self._criterionValue)

    @property
    def text(self) -> str:
        return self.buildText(False)

    @property
    def textForTooltip(self) -> str:
        return self.buildText(True)

    @property
    def basicText(self) -> str:
        return self._serverCriterionForm

    def clone(self) -> IItemCriterion:
        return ItemCriterion(self.basicText)

    def buildText(self, forTooltip: bool = False) -> str:
        readableCriterionRef: str = None
        knownCriteriaList: list = None
        index: int = 0

        if self._criterionRef == "CM":
            readableCriterionRef = I18n.getUiText("ui.stats.movementPoints")

        elif self._criterionRef == "CP":
            readableCriterionRef = I18n.getUiText("ui.stats.actionPoints")

        elif self._criterionRef == "CH":
            readableCriterionRef = I18n.getUiText("ui.pvp.honourPoints")

        elif self._criterionRef == "CD":
            readableCriterionRef = I18n.getUiText("ui.pvp.disgracePoints")

        elif self._criterionRef == "CT":
            readableCriterionRef = I18n.getUiText("ui.stats.takleBlock")

        elif self._criterionRef == "Ct":
            readableCriterionRef = I18n.getUiText("ui.stats.takleEvade")

        else:
            knownCriteriaList = [
                "CS",
                "Cs",
                "CV",
                "Cv",
                "CA",
                "Ca",
                "CI",
                "Ci",
                "CW",
                "Cw",
                "CC",
                "Cc",
                "PG",
                "PJ",
                "Pj",
                "PM",
                "PA",
                "PN",
                "PE",
                "<NO>",
                "PS",
                "PR",
                "PL",
                "PK",
                "Pg",
                "Pr",
                "Ps",
                "Pa",
                "PP",
                "PZ",
                "CM",
                "Qa",
                "CP",
                "ca",
                "cc",
                "ci",
                "cs",
                "cv",
                "cw",
                "Pl",
            ]
            index = knownCriteriaList.index(self._criterionRef)

        return (
            readableCriterionRef
            + " "
            + self._operator.text
            + " "
            + self._criterionValue
        )

    def getInfos(self) -> None:
        operator: str = None
        for operator in ItemCriterionOperator.OPERATORS_LIST:
            if self._serverCriterionForm.find(operator) == 2:
                self._operator = ItemCriterionOperator(operator)
                self._criterionRef = self._serverCriterionForm.split(operator)[0]
                self._criterionValue = self._serverCriterionForm.split(operator)[1]
                self._criterionValueText = self._serverCriterionForm.split(operator)[1]

    def getCriterion(self) -> int:
        criterion: int = 0
        player: PlayedCharacterManager = PlayedCharacterManager()
        statsManager: statsManager = statsManager()

        if statsManager == None:
            return 0

        stats: EntityStats = statsManager.getStats(player.id)

        if stats == None:
            return 0

        elif self._criterionRef == "Ca":
            criterion = stats.getStatBaseValue(StatIds.AGILITY)

        elif self._criterionRef == "CA":
            criterion = stats.getStatTotalValue(StatIds.AGILITY)

        elif self._criterionRef == "Cc":
            criterion = stats.getStatBaseValue(StatIds.CHANCE)

        elif self._criterionRef == "CC":
            criterion = stats.getStatTotalValue(StatIds.CHANCE)

        elif self._criterionRef == "Ce":
            criterion = stats.getStatBaseValue(StatIds.ENERGY_POINTS)

        elif self._criterionRef == "CE":
            criterion = stats.getStatTotalValue(StatIds.MAX_ENERGY_POINTS)

        elif self._criterionRef == "CH":
            criterion = stats.getStatTotalValue(StatIds.HONOUR_POINTS)

        elif self._criterionRef == "Ci":
            criterion = stats.getStatBaseValue(StatIds.INTELLIGENCE)

        elif self._criterionRef == "CI":
            criterion = stats.getStatTotalValue(StatIds.INTELLIGENCE)

        elif self._criterionRef == "CL":
            criterion = stats.getHealthPoints()

        elif self._criterionRef == "CM":
            criterion = stats.getStatTotalValue(StatIds.MOVEMENT_POINTS)

        elif self._criterionRef == "CP":
            criterion = stats.getStatTotalValue(StatIds.ACTION_POINTS)

        elif self._criterionRef == "Cs":
            criterion = stats.getStatBaseValue(StatIds.STRENGTH)

        elif self._criterionRef == "CS":
            criterion = stats.getStatTotalValue(StatIds.STRENGTH)

        elif self._criterionRef == "Cv":
            criterion = stats.getStatBaseValue(StatIds.VITALITY)

        elif self._criterionRef == "CV":
            criterion = stats.getStatTotalValue(StatIds.VITALITY)

        elif self._criterionRef == "Cw":
            criterion = stats.getStatBaseValue(StatIds.WISDOM)

        elif self._criterionRef == "CW":
            criterion = stats.getStatTotalValue(StatIds.WISDOM)

        elif self._criterionRef == "Ct":
            criterion = stats.getStatTotalValue(StatIds.TACKLE_EVADE)

        elif self._criterionRef == "CT":
            criterion = stats.getStatTotalValue(StatIds.TACKLE_BLOCK)

        elif self._criterionRef == "ca":
            criterion = stats.getStatAdditionalValue(StatIds.AGILITY)

        elif self._criterionRef == "cc":
            criterion = stats.getStatAdditionalValue(StatIds.CHANCE)

        elif self._criterionRef == "ci":
            criterion = stats.getStatAdditionalValue(StatIds.INTELLIGENCE)

        elif self._criterionRef == "cs":
            criterion = stats.getStatAdditionalValue(StatIds.STRENGTH)

        elif self._criterionRef == "cv":
            criterion = stats.getStatAdditionalValue(StatIds.VITALITY)

        elif self._criterionRef == "cw":
            criterion = stats.getStatAdditionalValue(StatIds.WISDOM)

        return criterion
