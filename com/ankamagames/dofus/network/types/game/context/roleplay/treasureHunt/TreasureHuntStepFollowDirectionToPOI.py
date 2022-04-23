from com.ankamagames.dofus.network.types.game.context.roleplay.treasureHunt.TreasureHuntStep import TreasureHuntStep


class TreasureHuntStepFollowDirectionToPOI(TreasureHuntStep):
    direction:int
    poiLabelId:int
    

    def init(self, direction_:int, poiLabelId_:int):
        self.direction = direction_
        self.poiLabelId = poiLabelId_
        
        super().__init__()
    
    