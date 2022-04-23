      
class floatOfMountBirthedCriterion(ItemCriterion, IDataCenter):
      
   
   function floatOfMountBirthedCriterion(pCriterion:str)
      super().__init__(pCriterion)
   
   @property
   def text(self) -> str:
      readableCriterionValue:str = _criterionValueText
      mountsBirthedCount:int = parseInt(readableCriterionValue.split(",")[1]) + 1
      return I18n.getUiText("ui.mount.mountsBirthedCount",[mountsBirthedCount])
   
   def clone(self) -> IItemCriterion:
      return floatOfMountBirthedCriterion(self.basicText)
   
   def getCriterion(self) -> int:
      return 0
