from com.ankamagames.dofus.network.types.game.context.fight.FightTeamMemberInformations import FightTeamMemberInformations


class FightTeamMemberTaxCollectorInformations(FightTeamMemberInformations):
    firstNameId:int
    lastNameId:int
    level:int
    guildId:int
    uid:int
    

    def init(self, firstNameId_:int, lastNameId_:int, level_:int, guildId_:int, uid_:int, id_:int):
        self.firstNameId = firstNameId_
        self.lastNameId = lastNameId_
        self.level = level_
        self.guildId = guildId_
        self.uid = uid_
        
        super().__init__(id_)
    
    