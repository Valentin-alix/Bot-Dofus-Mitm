from com.ankamagames.dofus.datacenter.jobs.Recipe import Recipe
from com.ankamagames.dofus.internalDatacenter.DataEnum import DataEnum
from com.ankamagames.dofus.internalDatacenter.items.ItemWrapper import ItemWrapper
from com.ankamagames.dofus.logic.game.common.misc.IStorageView import IStorageView
from com.ankamagames.dofus.logic.game.common.misc.inventoryView.StorageGenericView import (
    StorageGenericView,
)


class StorageCraftFilterView(StorageGenericView):

    _ingredients: dict

    _skillId: int

    _jobLevel: int

    _parent: IStorageView

    def __init__(self, parentView: IStorageView, skillId: int, jobLevel: int):
        recipe: Recipe = None
        selected: bool = False
        id: int = 0
        super().__init__()
        recipies: list = Recipe.getAllRecipesForSkillId(skillId, jobLevel)
        self._ingredients = dict()
        for recipe in recipies:
            selected = False
            for id in recipe.ingredientIds:
                self._ingredients[id] = True
        self._ingredients[DataEnum.ITEM_GID_SIGNATURE_RUNE] = True
        self._skillId = skillId
        self._jobLevel = jobLevel
        self._parent = parentView

    @property
    def name(self) -> str:
        return "storageCraftFilter"

    def isListening(self, item: ItemWrapper) -> bool:
        return self._parent.isListening(item) and self._ingredients.hasOwnProperty(
            item.objectGID
        )

    def updateView(self) -> None:
        super().updateView()

    @property
    def parent(self) -> IStorageView:
        return self._parent

    @parent.setter
    def parent(self, view: IStorageView) -> None:
        self._parent = view
