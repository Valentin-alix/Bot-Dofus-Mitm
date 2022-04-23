               
class SpellItemCriterion(ItemCriterion, IDataCenter):
      
   
   _spellId:int
   
   def __init__(self, pCriterion:str):
      super().__init__(pCriterion)
      arrayParams:list = str(_criterionValueText).split(",")
      if arrayParams and len(arrayParams) > 0:
         if len(arrayParams) <= 1:
            self._spellId = int(arrayParams[0])
      else:
         self._spellId = int(_criterionValue)
   
   @property
   def isRespected(self) -> bool:
      sp:SpellWrapper = None
      for sp in PlayedCharacterManager().playerSpellList:
         if sp.id == self._spellId:
            if _operator.text == ItemCriterionOperator.EQUAL:
               return True
            return False
      if _operator.text == ItemCriterionOperator.DIFFERENT:
         return True
      return False
   
   @property
   def text(self) -> str:
      readableCriterion:str = ""
      spell:Spell = Spell.getSpellById(self._spellId)
      if not spell:
         return readableCriterion
      readableCriterionValue:str = spell.name
      switch(_operator.text)
         case ItemCriterionOperator.EQUAL:
            readableCriterion = I18n.getUiText("ui.criterion.gotSpell",[readableCriterionValue])
            break
         case ItemCriterionOperator.DIFFERENT:
            readableCriterion = I18n.getUiText("ui.criterion.doesntGotSpell",[readableCriterionValue])
      return readableCriterion
   
   def clone(self) -> IItemCriterion:
      return SpellItemCriterion(self.basicText)
