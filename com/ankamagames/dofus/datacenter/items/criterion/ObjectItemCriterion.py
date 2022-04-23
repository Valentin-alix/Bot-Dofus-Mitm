               
class ObjectItemCriterion(ItemCriterion, IDataCenter):
      
   
   _criterionValueQuantity:int = -1
   
   def __init__(self, pCriterion:str):
      itemIdAndQuantity:list = None
      super().__init__(pCriterion)
      if _criterionValue == 0 and _criterionValueText.index(",") != -1:
         itemIdAndQuantity = _criterionValueText.split(",")
         _criterionValue = int(itemIdAndQuantity[0])
         self._criterionValueQuantity = int(itemIdAndQuantity[1])
         if self._criterionValueQuantity == 0 and str(itemIdAndQuantity[1]).index("0") == -1:
            self._criterionValueQuantity = -1
   
   @property
   def isRespected(self) -> bool:
      iw:ItemWrapper = None
      itemQuantity:int = 0
      for iw in InventoryManager().realInventory:
         if iw.objectGID == _criterionValue:
            itemQuantity = iw.quantity
            break
      if _operator.text == ItemCriterionOperator.EQUAL:
         return self._criterionValueQuantity == itemQuantity > 0 if -1 else itemQuantity == self._criterionValueQuantity
      if _operator.text == ItemCriterionOperator.DIFFERENT:
         return self._criterionValueQuantity == itemQuantity == 0 if -1 else itemQuantity != self._criterionValueQuantity
      if _operator.text == ItemCriterionOperator.SUPERIOR:
         return itemQuantity > max(self._criterionValueQuantity,0)
      if _operator.text == ItemCriterionOperator.INFERIOR:
         return itemQuantity < max(self._criterionValueQuantity,1)
      return False
   
   @property
   def text(self) -> str:
      objectName:str = Item.getItemById(_criterionValue).name
      readableCriterion:str = ""
      switch(_operator.text)
         case ItemCriterionOperator.DIFFERENT:
            if self._criterionValueQuantity == 1 or self._criterionValueQuantity == -1:
               readableCriterion = I18n.getUiText("ui.common.doNotPossess",[objectName])
            else:
               readableCriterion = I18n.getUiText("ui.common.doNotPossessQuantity",[self._criterionValueQuantity,objectName])
            break
         case ItemCriterionOperator.EQUAL:
            if self._criterionValueQuantity == 1 or self._criterionValueQuantity == -1:
               readableCriterion = I18n.getUiText("ui.common.doPossess",[objectName])
            else:
               readableCriterion = I18n.getUiText("ui.common.doPossessQuantity",[self._criterionValueQuantity,objectName])
            break
         case ItemCriterionOperator.SUPERIOR:
            if self._criterionValueQuantity == 0:
               readableCriterion = I18n.getUiText("ui.common.doPossess",[objectName])
            else:
               readableCriterion = I18n.getUiText("ui.common.doPossessQuantityOrMore",[self._criterionValueQuantity + 1,objectName])
            break
         case ItemCriterionOperator.INFERIOR:
            if self._criterionValueQuantity == 1:
               readableCriterion = I18n.getUiText("ui.common.doNotPossess",[objectName])
            else:
               readableCriterion = I18n.getUiText("ui.common.doPossessQuantityOrLess",[self._criterionValueQuantity - 1,objectName])
      return readableCriterion
   
   def clone(self) -> IItemCriterion:
      return ObjectItemCriterion(self.basicText)
