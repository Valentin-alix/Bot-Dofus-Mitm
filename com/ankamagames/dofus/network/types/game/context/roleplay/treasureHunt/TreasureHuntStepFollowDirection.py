from com.ankamagames.dofus.network.types.game.context.roleplay.treasureHunt.TreasureHuntStep import TreasureHuntStep


class TreasureHuntStepFollowDirection(TreasureHuntStep):
    direction:int
    mapCount:int
    

    def init(self, direction_:int, mapCount_:int):
        self.direction = direction_
        self.mapCount = mapCount_
        
        super().__init__()
    
    