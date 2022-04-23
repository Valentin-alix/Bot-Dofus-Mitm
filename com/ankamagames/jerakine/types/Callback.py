from types import FunctionType
from typing import Any


class Callback:

    method: FunctionType

    args: list

    def __init__(self, fMethod: FunctionType, *aArgs):
        super().__init__()
        self.method = fMethod
        self.args = aArgs

    @staticmethod
    def argFromlist(fMethod: FunctionType, args: list = None) -> "Callback":
        cb: Callback = Callback(fMethod)
        cb.args = args
        return cb

    def exec(self) -> Any:
        return self.method(None, self.args)
