from types import FunctionType
from typing import Any


class Treatment:
    def __init__(self, object, func: FunctionType, params: list):
        self._object = object
        self._calledFunctionType = func
        self._params = params

    @property
    def calledfunction(self) -> FunctionType:
        return self._calledFunctionType

    @property
    def params(self) -> list:
        return self._params

    @property
    def object(self) -> Any:
        return self._object

    def process(self) -> bool:
        self._calledFunctionType(self._object, self._params)
        return True

    def isSameTreatment(self, object, func: FunctionType, params: list) -> bool:
        if (
            object != self._object
            or func != self._calledFunctionType
            or len(self._params) != len(params)
        ):
            return False
        for i in range(0, len(self._params), 1):
            if params[i] != self._params[i]:
                return False
        return True

    def isCloseTreatment(self, object, func: FunctionType, params: list) -> bool:
        param = None
        if (
            object
            and object != self._object
            or func
            and func != self._calledFunctionType
        ):
            return False
        for param in params:
            if self._params.find(param) == -1:
                return False
        return True
