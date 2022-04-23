      
class CriterionUtils(IDataCenter):
      
   
   def __init__(self):
      super().__init__()
   
   def getCriteriaFromstr(self, pCriteriastrForm:str) -> list[IItemCriterion]:
      stringCriterion:str = None
      tabSingleCriteria:list = None
      stringCriterion2:str = None
      newGroupCriterion:GroupItemCriterion = None
      criteriastrForm:str = pCriteriastrForm
      criteria:list[IItemCriterion] = list[IItemCriterion]()
      if not criteriastrForm or len(criteriastrForm) == 0:
         return criteria
      tabParenthesis:list[str] = StringUtils.getDelimitedText(criteriastrForm,"(",")",True)
      for stringCriterion in tabParenthesis:
         newGroupCriterion = GroupItemCriterion(stringCriterion)
         criteria.append(newGroupCriterion)
         criteriastrForm = str.replace(criteriastrForm, stringCriterion, "")
      tabSingleCriteria = criteriastrForm.split(/[&|]/)
      for stringCriterion2 in tabSingleCriteria:
         if stringCriterion2 != "":
            criteria.append(ItemCriterionFactory.create(stringCriterion2))
      return criteria
