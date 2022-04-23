      
class floatOfItemMadeCriterion(ItemCriterion, IDataCenter):
      
   
   function floatOfItemMadeCriterion(pCriterion:str)
      super().__init__(pCriterion)
   
   @property
   def text(self) -> str:
      readableCriterionValue:str = _criterionValueText
      itemsMadeCount:int = parseInt(readableCriterionValue.split(",")[1]) + 1
      return I18n.getUiText("ui.smithmagic.itemsMadeCount",[itemsMadeCount])
   
   def clone(self) -> IItemCriterion:
      return floatOfItemMadeCriterion(self.basicText)
