         
class CommunityItemCriterion(ItemCriterion, IDataCenter):
      
   
   def __init__(self, pCriterion:str):
      super().__init__(pCriterion)
   
   @property
   def isRespected(self) -> bool:
      serverCommunity:int = PlayerManager().server.communityId
      switch(_operator.text)
         case ItemCriterionOperator.EQUAL:
            return serverCommunity == criterionValue
         case ItemCriterionOperator.DIFFERENT:
            return serverCommunity != criterionValue
         default:
            return False
   
   @property
   def text(self) -> str:
      readableCriterion:str = None
      readableCriterionValue:str = PlayerManager().server.community.name
      switch(_operator.text)
         case ItemCriterionOperator.EQUAL:
            readableCriterion = I18n.getUiText("ui.criterion.community",[readableCriterionValue])
            break
         case ItemCriterionOperator.DIFFERENT:
            readableCriterion = I18n.getUiText("ui.criterion.notCommunity",[readableCriterionValue])
      return readableCriterion
   
   def clone(self) -> IItemCriterion:
      return CommunityItemCriterion(self.basicText)
