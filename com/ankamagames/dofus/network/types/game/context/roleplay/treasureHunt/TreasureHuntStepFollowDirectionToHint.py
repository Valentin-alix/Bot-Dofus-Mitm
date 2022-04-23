from com.ankamagames.dofus.network.types.game.context.roleplay.treasureHunt.TreasureHuntStep import TreasureHuntStep


class TreasureHuntStepFollowDirectionToHint(TreasureHuntStep):
    direction:int
    npcId:int
    

    def init(self, direction_:int, npcId_:int):
        self.direction = direction_
        self.npcId = npcId_
        
        super().__init__()
    
    