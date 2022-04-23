from com.ankamagames.dofus.network.messages.game.context.roleplay.job.JobAllowMultiCraftRequestMessage import JobAllowMultiCraftRequestMessage


class JobMultiCraftAvailableSkillsMessage(JobAllowMultiCraftRequestMessage):
    playerId:int
    skills:list[int]
    

    def init(self, playerId_:int, skills_:list[int], enabled_:bool):
        self.playerId = playerId_
        self.skills = skills_
        
        super().__init__(enabled_)
    
    