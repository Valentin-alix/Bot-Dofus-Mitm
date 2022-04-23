                     
class QuestItemCriterion(ItemCriterion, IDataCenter):
      
   
   _questId:int
   
   def __init__(self, pCriterion:str):
      super().__init__(pCriterion)
      self._questId = _criterionValue
   
   @property
   def text(self) -> str:
      readableCriterion:str = ""
      quest:Quest = Quest.getQuestById(self._questId)
      if not quest:
         return readableCriterion
      readableCriterionValue:str = quest.name
      s:str = _serverCriterionForm.slice(0,2)
      switch(s)
         case "Qa":
            readableCriterion = I18n.getUiText("ui.grimoire.quest.active",[readableCriterionValue])
            break
         case "Qc":
            readableCriterion = I18n.getUiText("ui.grimoire.quest.startable",[readableCriterionValue])
            break
         case "Qf":
            readableCriterion = I18n.getUiText("ui.grimoire.quest.done",[readableCriterionValue])
      return readableCriterion
   
   @property
   def isRespected(self) -> bool:
      questFrame:QuestFrame = None
      completedQuests:list[int] = None
      questA:QuestActiveInformations = None
      quest:Quest = Quest.getQuestById(self._questId)
      if not quest:
         return False
      questFrame =Kernel().getWorker().getFrame(QuestFrame)
      s:str = _serverCriterionForm.slice(0,2)
      switch(s)
         case "Qa":
            for questA in questFrame.getActiveQuests():
               if questA.questId == self._questId:
                  return True
            break
         case "Qc":
            return True
         case "Qf":
            completedQuests = questFrame.getCompletedQuests()
            return !not completedQuests ? completedQuests.index(self._questId) != -1 : False
      return False
   
   def clone(self) -> IItemCriterion:
      return QuestItemCriterion(self.basicText)
   
   def getCriterion(self) -> int:
      return PlayedCharacterManager().infos.level
