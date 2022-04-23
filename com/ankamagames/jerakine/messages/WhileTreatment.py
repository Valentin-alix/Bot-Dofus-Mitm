from types import FunctionType
from com.ankamagames.jerakine.messages.Treatment import Treatment


class WhileTreatment(Treatment):
    def __init__(self, object, func: FunctionType, params: list):
        super().__init__(object, func, params)

    def process(self) -> bool:
        return not self.calledfunction(self.object, self.params)
