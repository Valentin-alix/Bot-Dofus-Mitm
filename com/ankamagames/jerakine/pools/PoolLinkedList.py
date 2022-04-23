import com.ankamagames.jerakine.pools.PoolsManager as poolsManager
from mx.utils.LinkedList import LinkedList
from mx.utils.LinkedListNode import LinkedListNode


class PoolLinkedList(LinkedList):
    def __init__(self):
        super().__init__()

    def makeNode(self, value) -> LinkedListNode:
        node: LinkedListNode = None
        node = poolsManager.PoolsManager().getLinkedListNodePool().checkOut()
        node.value = value
        return node
