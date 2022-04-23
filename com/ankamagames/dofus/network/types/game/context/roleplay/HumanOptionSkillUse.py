from com.ankamagames.dofus.network.types.game.context.roleplay.HumanOption import HumanOption


class HumanOptionSkillUse(HumanOption):
    elementId:int
    skillId:int
    skillEndTime:int
    

    def init(self, elementId_:int, skillId_:int, skillEndTime_:int):
        self.elementId = elementId_
        self.skillId = skillId_
        self.skillEndTime = skillEndTime_
        
        super().__init__()
    
    