               
from pyd2bot.dofus.datacenter.items.ItemCriterion import ItemCriterion


class SubareaItemCriterion(ItemCriterion):
      
   
   def __init__(self, pCriterion:str):
      super().__init__(pCriterion)
   
   @property
   def isRespected(self) -> bool:
      playerPosition:int = PlayedCharacterManager().currentSubArea.id
      switch(_operator.text)
         case ItemCriterionOperator.EQUAL:
         case ItemCriterionOperator.DIFFERENT:
            return super().isRespected
         default:
            return False
   
   @property
   def text(self) -> str:
      readableCriterion:str = None
      subArea:SubArea = SubArea.getSubAreaById(_criterionValue)
      if not subArea:
         return "error on subareaItemCriterion"
      zoneName:str = subArea.name
      switch(_operator.text)
         case ItemCriterionOperator.EQUAL:
            readableCriterion = I18n.getUiText("ui.tooltip.beInSubarea",[zoneName])
            break
         case ItemCriterionOperator.DIFFERENT:
            readableCriterion = I18n.getUiText("ui.tooltip.dontBeInSubarea",[zoneName])
      return readableCriterion
   
   def clone(self) -> IItemCriterion:
      return SubareaItemCriterion(self.basicText)
   
   def getCriterion(self) -> int:
      return PlayedCharacterManager().currentSubArea.id
