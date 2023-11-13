from dataclasses import dataclass

from app.types_ import MagicPoolStatus
from app.types_.dofus.scripts.com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem


@dataclass
class Fm:
    current_item: ObjectItem
    remainder: int = 0

    def get_remainder(self, new_item: ObjectItem, magic_pool_status: MagicPoolStatus):
        if magic_pool_status != MagicPoolStatus.NEUTRAL:
            ...
            # Get weight by actionId * value effect
            # self.current_item.effects[0].
