from types import FunctionType


class IDragAndDropHandler:
    @property
    def dropValidator(self) -> FunctionType:
        pass

    @dropValidator.setter
    def dropValidator(self, param1: FunctionType) -> None:
        pass

    @property
    def removeDropSource(self) -> FunctionType:
        pass

    @removeDropSource.setter
    def removeDropSource(self, param1: FunctionType) -> None:
        pass

    @property
    def processDrop(self) -> FunctionType:
        pass

    @processDrop.setter
    def processDrop(self, param1: FunctionType) -> None:
        pass
