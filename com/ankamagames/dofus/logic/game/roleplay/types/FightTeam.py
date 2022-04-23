from com.ankamagames.dofus.kernel.Kernel import Kernel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from com.ankamagames.dofus.logic.game.roleplay.types.Fight import Fight
from com.ankamagames.dofus.network.enums.FightOptionsEnum import FightOptionsEnum
from com.ankamagames.dofus.network.types.game.context.GameContextActorInformations import (
    GameContextActorInformations,
)
from com.ankamagames.dofus.network.types.game.context.fight.FightOptionsInformations import (
    FightOptionsInformations,
)
from com.ankamagames.dofus.network.types.game.context.fight.FightTeamInformations import (
    FightTeamInformations,
)
from com.ankamagames.dofus.network.types.game.context.fight.FightTeamMemberCharacterInformations import (
    FightTeamMemberCharacterInformations,
)
from com.ankamagames.dofus.network.types.game.context.fight.FightTeamMemberInformations import (
    FightTeamMemberInformations,
)
from com.ankamagames.dofus.types.entities.AnimatedCharacter import AnimatedCharacter
from com.ankamagames.jerakine.entities.interfaces.IEntity import IEntity
from com.ankamagames.jerakine.logger.Logger import Logger


class FightTeam(GameContextActorInformations):

    logger = Logger(__name__)

    fight: "Fight"

    teamType: int

    teamEntity: IEntity

    teamInfos: FightTeamInformations

    teamOptions: list

    def __init__(
        self,
        fight: "Fight",
        teamType: int,
        teamEntity: IEntity,
        teamInfos: FightTeamInformations,
        teamOptions: FightOptionsInformations,
    ):
        super().__init__()
        self.fight = fight
        self.teamType = teamType
        self.teamEntity = teamEntity
        self.teamInfos = teamInfos
        self.teamOptions = [False] * 4
        self.teamOptions[
            FightOptionsEnum.FIGHT_OPTION_ASK_FOR_HELP.value
        ] = teamOptions.isAskingForHelp
        self.teamOptions[
            FightOptionsEnum.FIGHT_OPTION_SET_CLOSED.value
        ] = teamOptions.isClosed
        self.teamOptions[
            FightOptionsEnum.FIGHT_OPTION_SET_SECRET.value
        ] = teamOptions.isSecret
        self.teamOptions[
            FightOptionsEnum.FIGHT_OPTION_SET_TO_PARTY_ONLY.value
        ] = teamOptions.isRestrictedToPartyOnly

    def hasGroupMember(self) -> bool:
        partyMember: PartyMemberWrapper = None
        fightTeamMember: FightTeamMemberInformations = None
        teamHasGroupMember: bool = False
        pmf: PartyManagementFrame = Kernel.getWorker().getFrame(PartyManagementFrame)
        partyMemberNames: list[str] = list[str]()
        for partyMember in pmf.partyMembers:
            partyMemberNames.append(partyMember.name)
        for fightTeamMember in self.teamInfos.teamMembers:
            if (
                fightTeamMember
                and isinstance(fightTeamMember, FightTeamMemberCharacterInformations)
                and FightTeamMemberCharacterInformations(fightTeamMember).name
                in partyMemberNames
            ):
                teamHasGroupMember = True
        return teamHasGroupMember

    def hasOptions(self) -> bool:
        opt = None
        hasOptions: bool = False
        for opt in self.teamOptions:
            if self.teamOptions.get(opt):
                hasOptions = True
        return hasOptions
