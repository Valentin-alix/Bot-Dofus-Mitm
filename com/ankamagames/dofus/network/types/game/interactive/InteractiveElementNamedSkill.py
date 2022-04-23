from com.ankamagames.dofus.network.types.game.interactive.InteractiveElementSkill import InteractiveElementSkill


class InteractiveElementNamedSkill(InteractiveElementSkill):
    nameId:int
    

    def init(self, nameId_:int, skillId_:int, skillInstanceUid_:int):
        self.nameId = nameId_
        
        super().__init__(skillId_, skillInstanceUid_)
    
    