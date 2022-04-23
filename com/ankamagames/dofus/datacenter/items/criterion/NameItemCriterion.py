         
class NameItemCriterion(ItemCriterion, IDataCenter):
      
   
   def __init__(self, pCriterion:str):
      super().__init__(pCriterion)
   
   @property
   def text(self) -> str:
      readableCriterionRef:str = I18n.getUiText("ui.common.name")
      return readableCriterionRef + " " + self.getReadableOperator()
   
   @property
   def isRespected(self) -> bool:
      name:str = PlayedCharacterManager().infos.name
      respected = False
      criterionValue:str = str(_criterionValue)
      switch(_operator.text)
         case "=":
            respected = name == criterionValue
            break
         case "!":
            respected = name != criterionValue
            break
         case "~":
            respected = name.toLowerCase() == criterionValue.toLowerCase()
            break
         case "S":
            respected = name.toLowerCase().index(criterionValue.toLowerCase()) == 0
            break
         case "s":
            respected = name.index(criterionValue) == 0
            break
         case "E":
            respected = name.toLowerCase().index(criterionValue.toLowerCase()) == len(name) - len(criterionValue)
            break
         case "e":
            respected = name.index(criterionValue) == len(name) - len(criterionValue)
            break
         case "v":
            break
         case "i":
      return respected
   
   def clone(self) -> IItemCriterion:
      return NameItemCriterion(self.basicText)
   
   def getCriterion(self) -> int:
      return 0
   
   def getReadableOperator(self) -> str:
      text:str = ""
      logger.debug("operator : " + _operator)
      switch(_operator.text)
         case "!":
         case "=":
            text = _operator.text + " " + _criterionValueText
            break
         case "~":
            text = "= " + _criterionValueText
            break
         case "S":
         case "s":
            text = I18n.getUiText("ui.criterion.startWith",[_criterionValueText])
            break
         case "E":
         case "e":
            text = I18n.getUiText("ui.criterion.endWith",[_criterionValueText])
            break
         case "v":
            text = I18n.getUiText("ui.criterion.valid")
            break
         case "i":
            text = I18n.getUiText("ui.criterion.invalid")
      return text
