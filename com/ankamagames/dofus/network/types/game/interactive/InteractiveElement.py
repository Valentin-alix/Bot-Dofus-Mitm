from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.interactive.InteractiveElementSkill import InteractiveElementSkill
    from com.ankamagames.dofus.network.types.game.interactive.InteractiveElementSkill import InteractiveElementSkill
    


class InteractiveElement(NetworkMessage):
    elementId:int
    elementTypeId:int
    enabledSkills:list['InteractiveElementSkill']
    disabledSkills:list['InteractiveElementSkill']
    onCurrentMap:bool
    

    def init(self, elementId_:int, elementTypeId_:int, enabledSkills_:list['InteractiveElementSkill'], disabledSkills_:list['InteractiveElementSkill'], onCurrentMap_:bool):
        self.elementId = elementId_
        self.elementTypeId = elementTypeId_
        self.enabledSkills = enabledSkills_
        self.disabledSkills = disabledSkills_
        self.onCurrentMap = onCurrentMap_
        
        super().__init__()
    
    