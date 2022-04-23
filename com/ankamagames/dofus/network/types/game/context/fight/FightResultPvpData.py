from com.ankamagames.dofus.network.types.game.context.fight.FightResultAdditionalData import FightResultAdditionalData


class FightResultPvpData(FightResultAdditionalData):
    grade:int
    minHonorForGrade:int
    maxHonorForGrade:int
    honor:int
    honorDelta:int
    

    def init(self, grade_:int, minHonorForGrade_:int, maxHonorForGrade_:int, honor_:int, honorDelta_:int):
        self.grade = grade_
        self.minHonorForGrade = minHonorForGrade_
        self.maxHonorForGrade = maxHonorForGrade_
        self.honor = honor_
        self.honorDelta = honorDelta_
        
        super().__init__()
    
    