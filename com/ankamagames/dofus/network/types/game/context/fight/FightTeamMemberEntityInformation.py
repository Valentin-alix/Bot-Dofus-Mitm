from com.ankamagames.dofus.network.types.game.context.fight.FightTeamMemberInformations import FightTeamMemberInformations


class FightTeamMemberEntityInformation(FightTeamMemberInformations):
    entityModelId:int
    level:int
    masterId:int
    

    def init(self, entityModelId_:int, level_:int, masterId_:int, id_:int):
        self.entityModelId = entityModelId_
        self.level = level_
        self.masterId = masterId_
        
        super().__init__(id_)
    
    