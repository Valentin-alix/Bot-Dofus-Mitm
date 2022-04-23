from com.ankamagames.dofus.network.types.game.interactive.skill.SkillActionDescription import SkillActionDescription


class SkillActionDescriptionTimed(SkillActionDescription):
    time:int
    

    def init(self, time_:int, skillId_:int):
        self.time = time_
        
        super().__init__(skillId_)
    
    