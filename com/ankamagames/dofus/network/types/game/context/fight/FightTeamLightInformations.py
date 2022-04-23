from com.ankamagames.dofus.network.types.game.context.fight.AbstractFightTeamInformations import AbstractFightTeamInformations


class FightTeamLightInformations(AbstractFightTeamInformations):
    teamMembersCount:int
    meanLevel:int
    hasFriend:bool
    hasGuildMember:bool
    hasAllianceMember:bool
    hasGroupMember:bool
    hasMyTaxCollector:bool
    hasFriend:bool
    hasGuildMember:bool
    hasAllianceMember:bool
    hasGroupMember:bool
    hasMyTaxCollector:bool
    

    def init(self, teamMembersCount_:int, meanLevel_:int, hasFriend_:bool, hasGuildMember_:bool, hasAllianceMember_:bool, hasGroupMember_:bool, hasMyTaxCollector_:bool, teamId_:int, leaderId_:int, teamSide_:int, teamTypeId_:int, nbWaves_:int):
        self.teamMembersCount = teamMembersCount_
        self.meanLevel = meanLevel_
        self.hasFriend = hasFriend_
        self.hasGuildMember = hasGuildMember_
        self.hasAllianceMember = hasAllianceMember_
        self.hasGroupMember = hasGroupMember_
        self.hasMyTaxCollector = hasMyTaxCollector_
        
        super().__init__(teamId_, leaderId_, teamSide_, teamTypeId_, nbWaves_)
    
    