from com.ankamagames.dofus.network.types.game.interactive.InteractiveElement import InteractiveElement
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.interactive.InteractiveElementSkill import InteractiveElementSkill
    from com.ankamagames.dofus.network.types.game.interactive.InteractiveElementSkill import InteractiveElementSkill
    


class InteractiveElementWithAgeBonus(InteractiveElement):
    ageBonus:int
    

    def init(self, ageBonus_:int, elementId_:int, elementTypeId_:int, enabledSkills_:list['InteractiveElementSkill'], disabledSkills_:list['InteractiveElementSkill'], onCurrentMap_:bool):
        self.ageBonus = ageBonus_
        
        super().__init__(elementId_, elementTypeId_, enabledSkills_, disabledSkills_, onCurrentMap_)
    
    