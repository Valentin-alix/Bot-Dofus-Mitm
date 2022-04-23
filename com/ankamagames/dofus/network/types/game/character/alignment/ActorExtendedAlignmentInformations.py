from com.ankamagames.dofus.network.types.game.character.alignment.ActorAlignmentInformations import ActorAlignmentInformations


class ActorExtendedAlignmentInformations(ActorAlignmentInformations):
    honor:int
    honorGradeFloor:int
    honorNextGradeFloor:int
    aggressable:int
    

    def init(self, honor_:int, honorGradeFloor_:int, honorNextGradeFloor_:int, aggressable_:int, alignmentSide_:int, alignmentValue_:int, alignmentGrade_:int, characterPower_:int):
        self.honor = honor_
        self.honorGradeFloor = honorGradeFloor_
        self.honorNextGradeFloor = honorNextGradeFloor_
        self.aggressable = aggressable_
        
        super().__init__(alignmentSide_, alignmentValue_, alignmentGrade_, characterPower_)
    
    