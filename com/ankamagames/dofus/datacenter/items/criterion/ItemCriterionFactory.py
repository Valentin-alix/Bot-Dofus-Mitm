from com.ankamagames.dofus.datacenter.items.criterion.ItemCriterion import ItemCriterion
from com.ankamagames.dofus.datacenter.items.criterion.QuestObjectiveItemCriterion import (
    QuestObjectiveItemCriterion,
)
from com.ankamagames.dofus.datacenter.items.criterion.SubscribeItemCriterion import (
    SubscribeItemCriterion,
)
from com.ankamagames.jerakine.logger.Logger import Logger
from com.ankamagames.dofus.datacenter.items.criterion.IItemCriterion import (
    IItemCriterion,
)
from com.ankamagames.dofus.datacenter.items.criterion.UnusableItemCriterion import (
    UnusableItemCriterion,
)

logger = Logger(__name__)


class ItemCriterionFactory:
    def create(pServerCriterionForm: str) -> IItemCriterion:
        criterion = None
        s: str = pServerCriterionForm[0:2]

        if s == "BI":
            criterion = UnusableItemCriterion(pServerCriterionForm)

        elif s in [
            "Ca",
            "CA",
            "ca",
            "Cc",
            "CC",
            "cc",
            "CD",
            "Ce",
            "CE",
            "CH",
            "Ci",
            "CI",
            "ci",
            "CL",
            "CM",
            "CP",
            "Cs",
            "CS",
            "cs",
            "Ct",
            "CT",
            "Cv",
            "CV",
            "cv",
            "Cw",
            "CW",
            "cw",
        ]:
            criterion = ItemCriterion(pServerCriterionForm)

        elif s == "EA":
            criterion = MonsterGroupChallengeCriterion(pServerCriterionForm)

        elif s == "EB":
            criterion = floatOfMountBirthedCriterion(pServerCriterionForm)

        elif s == "Ec":
            criterion = floatOfItemMadeCriterion(pServerCriterionForm)

        elif s == "Eu":
            criterion = RuneByBreakingItemCriterion(pServerCriterionForm)

        elif s == "Kd":
            criterion = ArenaDuelRankCriterion(pServerCriterionForm)

        elif s == "KD":
            from com.ankamagames.dofus.datacenter.items.criterion.ArenaMaxDuelRankCriterion import (
                ArenaMaxDuelRankCriterion,
            )

            criterion = ArenaMaxDuelRankCriterion(pServerCriterionForm)

        elif s == "Ks":
            from com.ankamagames.dofus.datacenter.items.criterion.ArenaSoloRankCriterion import (
                ArenaSoloRankCriterion,
            )

            criterion = ArenaSoloRankCriterion(pServerCriterionForm)

        elif s == "KS":
            from com.ankamagames.dofus.datacenter.items.criterion.ArenaMaxSoloRankCriterion import (
                ArenaMaxSoloRankCriterion,
            )

            criterion = ArenaMaxSoloRankCriterion(pServerCriterionForm)

        elif s == "Kt":
            criterion = ArenaTeamRankCriterion(pServerCriterionForm)

        elif s == "KT":
            criterion = ArenaMaxTeamRankCriterion(pServerCriterionForm)

        elif s == "MK":
            criterion = MapCharactersItemCriterion(pServerCriterionForm)

        elif s == "Oa":
            criterion = AchievementPointsItemCriterion(pServerCriterionForm)

        elif s == "OA":
            criterion = AchievementItemCriterion(pServerCriterionForm)

        elif s == "Ob":
            criterion = AchievementAccountItemCriterion(pServerCriterionForm)

        elif s == "Of":
            criterion = MountFamilyItemCriterion(pServerCriterionForm)

        elif s == "OH":
            criterion = NewHavenbagItemCriterion(pServerCriterionForm)

        elif s == "OO":
            criterion = AchievementObjectiveValidated(pServerCriterionForm)

        elif s == "Os":
            criterion = SmileyPackItemCriterion(pServerCriterionForm)

        elif s == "OV":
            criterion = SubscriptionDurationItemCriterion(pServerCriterionForm)

        elif s == "Ow":
            criterion = AllianceItemCriterion(pServerCriterionForm)

        elif s == "Ox":
            criterion = AllianceRightsItemCriterion(pServerCriterionForm)

        elif s == "Oz":
            criterion = AllianceAvAItemCriterion(pServerCriterionForm)

        elif s == "Pa":
            from com.ankamagames.dofus.datacenter.items.criterion.AlignmentLevelItemCriterion import (
                AlignmentLevelItemCriterion,
            )

            criterion = AlignmentLevelItemCriterion(pServerCriterionForm)

        elif s == "PA":
            criterion = SoulStoneItemCriterion(pServerCriterionForm)

        elif s == "Pb":
            criterion = FriendlistItemCriterion(pServerCriterionForm)

        elif s == "PB":
            criterion = SubareaItemCriterion(pServerCriterionForm)

        elif s == "Pe":
            criterion = PremiumAccountItemCriterion(pServerCriterionForm)

        elif s == "PE":
            criterion = EmoteItemCriterion(pServerCriterionForm)

        elif s == "Pf":
            criterion = RideItemCriterion(pServerCriterionForm)

        elif s == "Pg":
            criterion = GiftItemCriterion(pServerCriterionForm)

        elif s == "PG":
            criterion = BreedItemCriterion(pServerCriterionForm)

        elif s in ["Pi", "PI"]:
            criterion = SkillItemCriterion(pServerCriterionForm)

        elif s in ["PJ", "Pj"]:
            criterion = JobItemCriterion(pServerCriterionForm)

        elif s == "Pk":
            criterion = BonusSetItemCriterion(pServerCriterionForm)

        elif s == "PK":
            criterion = KamaItemCriterion(pServerCriterionForm)

        elif s == "PL":
            from com.ankamagames.dofus.datacenter.items.criterion.LevelItemCriterion import (
                LevelItemCriterion,
            )

            criterion = LevelItemCriterion(pServerCriterionForm)

        elif s == "Pl":
            criterion = PrestigeLevelItemCriterion(pServerCriterionForm)

        elif s == "Pm":
            criterion = MapItemCriterion(pServerCriterionForm)

        elif s == "PN":
            criterion = NameItemCriterion(pServerCriterionForm)

        elif s == "PO":
            criterion = ObjectItemCriterion(pServerCriterionForm)

        elif s == "Po":
            criterion = AreaItemCriterion(pServerCriterionForm)

        elif s in ["Pp", "PP"]:
            criterion = PVPRankItemCriterion(pServerCriterionForm)

        elif s == "Pr":
            criterion = SpecializationItemCriterion(pServerCriterionForm)

        elif s == "PR":
            criterion = MariedItemCriterion(pServerCriterionForm)

        elif s == "Ps":
            criterion = AlignmentItemCriterion(pServerCriterionForm)

        elif s == "PS":
            criterion = SexItemCriterion(pServerCriterionForm)

        elif s == "PT":
            criterion = SpellItemCriterion(pServerCriterionForm)

        elif s == "PU":
            criterion = BonesItemCriterion(pServerCriterionForm)

        elif s == "Pw":
            criterion = GuildItemCriterion(pServerCriterionForm)

        elif s == "PW":
            criterion = WeightItemCriterion(pServerCriterionForm)

        elif s == "Px":
            criterion = GuildRightsItemCriterion(pServerCriterionForm)

        elif s == "PX":
            criterion = AccountRightsItemCriterion(pServerCriterionForm)

        elif s == "Py":
            criterion = GuildLevelItemCriterion(pServerCriterionForm)

        elif s in ["Pz", "PZ"]:
            criterion = SubscribeItemCriterion(pServerCriterionForm)

        elif s in ["Qa", "Qc", "Qf"]:
            criterion = QuestItemCriterion(pServerCriterionForm)

        elif s == "Qo":
            criterion = QuestObjectiveItemCriterion(pServerCriterionForm)

        elif s == "SC":
            criterion = ServerTypeItemCriterion(pServerCriterionForm)

        elif s == "Sc":
            criterion = StaticCriterionItemCriterion(pServerCriterionForm)

        elif s == "Sd":
            criterion = DayItemCriterion(pServerCriterionForm)

        elif s == "SG":
            criterion = MonthItemCriterion(pServerCriterionForm)

        elif s == "SI":
            criterion = ServerItemCriterion(pServerCriterionForm)

        elif s == "ST":
            criterion = ServerSeasonTemporisCriterion(pServerCriterionForm)

        elif s == "Sy":
            criterion = CommunityItemCriterion(pServerCriterionForm)

        else:
            logger.warn(
                "Criterion '" + s + "' unknow or unused (" + pServerCriterionForm + ")"
            )

        return criterion
