from com.ankamagames.dofus.network.types.game.social.GuildVersatileInformations import GuildVersatileInformations


class GuildInAllianceVersatileInformations(GuildVersatileInformations):
    allianceId:int
    

    def init(self, allianceId_:int, guildId_:int, leaderId_:int, guildLevel_:int, nbMembers_:int):
        self.allianceId = allianceId_
        
        super().__init__(guildId_, leaderId_, guildLevel_, nbMembers_)
    
    