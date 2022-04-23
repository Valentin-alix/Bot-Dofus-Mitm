from asyncio.log import logger
from com.ankamagames.dofus.datacenter.jobs.Job import Job
from com.ankamagames.dofus.datacenter.jobs.Skill import Skill
from com.ankamagames.dofus.internalDatacenter.DataEnum import DataEnum
from com.ankamagames.dofus.internalDatacenter.items.ItemWrapper import ItemWrapper
from com.ankamagames.dofus.misc.utils.GameDataQuery import GameDataQuery
from com.ankamagames.dofus.types.IdAccessors import IdAccessors
from com.ankamagames.jerakine.data.GameData import GameData
from com.ankamagames.jerakine.data.I18n import I18n
from com.ankamagames.jerakine.data.I18nFileAccessor import I18nFileAccessor
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter


class Recipe(IDataCenter):

    MODULE: str = "Recipes"

    _jobRecipes: list

    resultId: int

    resultNameId: int

    resultTypeId: int

    resultLevel: int

    ingredientIds: list[int]

    quantities: list[int]

    jobId: int

    skillId: int

    changeVersion: str

    tooltipExpirationDate: float = None

    _result: ItemWrapper = None

    _resultName: str = None

    _ingredients: list[ItemWrapper] = None

    _job: Job = None

    _skill: Skill = None

    _words: str = None

    def __init__(self):
        super().__init__()

    @classmethod
    def getRecipeByResultId(cls, resultId: int) -> "Recipe":
        return GameData.getObject(cls.MODULE, resultId)

    @classmethod
    def getAllRecipesForSkillId(cls, pSkillId: int, jobLevel: int) -> list["Recipe"]:
        recipes: list[Recipe] = list()
        craftables: list[int] = Skill.getSkillById(pSkillId).craftableItemIds
        for resultId in craftables:
            recipe = cls.getRecipeByResultId(resultId)
            if recipe:
                if recipe.resultLevel <= jobLevel:
                    recipes.append(recipe)
        return recipes.sort(reverse=True, key=lambda e: e.resultLevel)

    @classmethod
    def getAllRecipes(cls) -> list["Recipe"]:
        return GameData.getObjects(cls.MODULE)

    idAccessors: IdAccessors = IdAccessors(None, getAllRecipes)

    @classmethod
    def getRecipesByJobId(cls, jobId: int) -> list:
        if jobId == DataEnum.JOB_ID_BASE:
            return None
        if not cls._jobRecipes:
            cls._jobRecipes = dict()
        if cls._jobRecipes.get(jobId):
            return cls._jobRecipes[jobId]
        results: list = list()
        recipeIds: list[int] = GameDataQuery.queryEquals(Recipe, "jobId", jobId)
        for recipeId in recipeIds:
            results.append(GameData.getObject(cls.MODULE, recipeId))
        cls._jobRecipes[jobId] = results
        return results

    @property
    def result(self) -> ItemWrapper:
        if not self._result:
            self._result = ItemWrapper.create(0, 0, self.resultId, 0, None, False)
        return self._result

    @property
    def resultName(self) -> str:
        if not self._resultName:
            self._resultName = I18n.getText(self.resultNameId)
        return self._resultName

    @property
    def ingredients(self) -> list[ItemWrapper]:
        if not self._ingredients:
            ingredientsCount = len(self.ingredientIds)
            self._ingredients = [True] * ingredientsCount
            for i in range(ingredientsCount):
                self._ingredients[i] = ItemWrapper.create(
                    0, 0, self.ingredientIds[i], self.quantities[i], [], False
                )
        return self._ingredients

    @property
    def words(self) -> str:
        if not self._words:
            self._words = I18nFileAccessor().getUnDiacriticalText(self.resultNameId)
            for ingredient in self.ingredients:
                self._words += " " + I18nFileAccessor().getUnDiacriticalText(
                    ingredient.nameId
                )
            self._words = self._words.toLowerCase()
        return self._words

    @property
    def job(self) -> Job:
        if not self._job:
            self._job = Job.getJobById(self.jobId)
        return self._job

    @property
    def skill(self) -> Skill:
        if not self._skill:
            self._skill = Skill.getSkillById(self.skillId)
        return self._skill
