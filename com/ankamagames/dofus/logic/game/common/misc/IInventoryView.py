from com.ankamagames.dofus.internalDatacenter.items.ItemWrapper import ItemWrapper


class IInventoryView:
    def initialize(self, param1: list[ItemWrapper]) -> None:
        pass

    @property
    def name(self) -> str:
        pass

    @property
    def content(self) -> list[ItemWrapper]:
        pass

    def addItem(self, param1: ItemWrapper, param2: int, param3: bool = True) -> None:
        pass

    def removeItem(self, param1: ItemWrapper, param2: int) -> None:
        pass

    def modifyItem(self, param1: ItemWrapper, param2: ItemWrapper, param3: int) -> None:
        pass

    def isListening(self, param1: ItemWrapper) -> bool:
        pass

    def updateView(self) -> None:
        pass

    def empty(self) -> None:
        pass
