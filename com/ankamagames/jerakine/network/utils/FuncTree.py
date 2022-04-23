from types import FunctionType
from com.ankamagames.jerakine.network.CustomDataWrapper import ByteArray


class FuncTree:
    def __init__(self, parent: "FuncTree" = None, func: FunctionType = None):
        super().__init__()
        self._parent = parent
        self._func = func
        self._index = 0
        self._current: "FuncTree" = None
        self._children: list["FuncTree"] = None
        self._input: ByteArray = None

    @property
    def children(self) -> list["FuncTree"]:
        return self._children

    def setRoot(self, input: ByteArray) -> None:
        self._input = input
        self._current = self

    def addChild(self, func: FunctionType) -> "FuncTree":
        child: FuncTree = FuncTree(self, func)
        if self._children == None:
            self._children = list[FuncTree]()
        self._children.append(child)
        return child

    def next(self) -> bool:
        self._current._func(self._input)
        if self.goDown():
            return True
        return self.goUp()

    def goUp(self) -> bool:
        while True:
            self._current = self._current._parent
            if self._current._index != len(self._current._children):
                break
            if self._current._parent == None:
                return False
        self._current = self._current._children[self._current._index]
        self._current._index += 1
        return True

    def goDown(self) -> bool:
        if self._current._children == None:
            return False
        if self._current._index == len(self._current._children):
            return False
        self._current = self._current._children[self._current._index]
        self._current._index += 1
        return True
