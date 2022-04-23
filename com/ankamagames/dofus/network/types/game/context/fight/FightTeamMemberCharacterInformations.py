from com.ankamagames.dofus.network.types.game.context.fight.FightTeamMemberInformations import FightTeamMemberInformations


class FightTeamMemberCharacterInformations(FightTeamMemberInformations):
    name:str
    level:int
    

    def init(self, name_:str, level_:int, id_:int):
        self.name = name_
        self.level = level_
        
        super().__init__(id_)
    
    