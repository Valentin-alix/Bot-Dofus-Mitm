from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ActorAlignmentInformations(NetworkMessage):
    alignmentSide:int
    alignmentValue:int
    alignmentGrade:int
    characterPower:int
    

    def init(self, alignmentSide_:int, alignmentValue_:int, alignmentGrade_:int, characterPower_:int):
        self.alignmentSide = alignmentSide_
        self.alignmentValue = alignmentValue_
        self.alignmentGrade = alignmentGrade_
        self.characterPower = characterPower_
        
        super().__init__()
    
    