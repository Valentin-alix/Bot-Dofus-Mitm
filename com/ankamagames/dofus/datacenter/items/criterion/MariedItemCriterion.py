      
class MariedItemCriterion(ItemCriterion, IDataCenter):
      
   
   def __init__(self, pCriterion:str):
      super().__init__(pCriterion)
   
   @property
   def text(self) -> str:
      readableCriterion:str = ""
      switch(_operator.text)
         case ItemCriterionOperator.EQUAL:
            if _criterionValue == 1:
               readableCriterion = I18n.getUiText("ui.tooltip.beMaried")
            else:
               readableCriterion = I18n.getUiText("ui.tooltip.beSingle")
            break
         case ItemCriterionOperator.DIFFERENT:
            if _criterionValue == 2:
               readableCriterion = I18n.getUiText("ui.tooltip.beMaried")
            else:
               readableCriterion = I18n.getUiText("ui.tooltip.beSingle")
      return readableCriterion
   
   def clone(self) -> IItemCriterion:
      return MariedItemCriterion(self.basicText)
   
   def getCriterion(self) -> int:
      return 0
