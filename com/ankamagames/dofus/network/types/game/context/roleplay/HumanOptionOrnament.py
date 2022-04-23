from com.ankamagames.dofus.network.types.game.context.roleplay.HumanOption import HumanOption


class HumanOptionOrnament(HumanOption):
    ornamentId:int
    level:int
    leagueId:int
    ladderPosition:int
    

    def init(self, ornamentId_:int, level_:int, leagueId_:int, ladderPosition_:int):
        self.ornamentId = ornamentId_
        self.level = level_
        self.leagueId = leagueId_
        self.ladderPosition = ladderPosition_
        
        super().__init__()
    
    