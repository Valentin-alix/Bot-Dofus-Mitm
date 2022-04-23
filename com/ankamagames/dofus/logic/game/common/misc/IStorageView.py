from com.ankamagames.dofus.logic.game.common.misc.IInventoryView import IInventoryView


class IStorageView(IInventoryView):
    @property
    def types(self) -> dict:
        pass
