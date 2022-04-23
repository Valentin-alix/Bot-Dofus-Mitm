from com.ankamagames.jerakine.utils.misc.Priotizable import Prioritizable


class PriorityComparer:
    def __init__(self):
        super().__init__()

    def compare(self, x: Prioritizable, y: Prioritizable) -> float:
        if x.priority > y.priority:
            return -1
        if x.priority < y.priority:
            return 1
        return 0
