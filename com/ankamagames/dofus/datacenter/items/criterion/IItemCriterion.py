class IItemCriterion:
    @property
    def inlineCriteria(self) -> list["IItemCriterion"]:
        pass

    @property
    def isRespected(self) -> bool:
        pass

    def clone(self) -> "IItemCriterion":
        pass
